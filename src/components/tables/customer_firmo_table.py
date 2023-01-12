import pandas as pd
from dash import Dash, html, Input, Output, dcc, dash_table, State
from src.components.Ids import ids
from src.components.data.load_data import  COLNAMES
from src.components.data.data_uploader import parse_data

def render(app: Dash) -> html.Div:

    @app.callback(
        Output(ids.cust_firmo_id, 'children'),
        Input(ids.cust_dropdown_id, 'value'),
        State(ids.upload_botton, 'contents'), # to call the data
        State(ids.upload_botton, 'filename') # to call the data
    )
    def update_cust_firmo_table(customer: list[str],contents, filename):
        if customer==None:
            return dcc.Textarea(value='Please select a customer', style={'color': 'red'})
        #call the data-------------------------------------------
        if contents:
            contents = contents[0]
            filename = filename[0]
            data = parse_data(contents, filename)
        #--------------------------------------------
            df = data.query("`Cleaned Parent Customer` in @customer")[COLNAMES.l_col_id + COLNAMES.l_col_firm]
            return html.Div(dash_table.DataTable(data=df.to_dict('records'),
                                                 columns=[{"name": i, "id": i} for i in df.columns],
                                                 # export_format='csv',
                                                 style_cell={'textAlign': 'center'},
                                                 style_header={'backgroundColor': 'grey', 'color': 'black', 'fontWeight': 'bold'},
                                                 style_data={'backgroundColor': 'white', 'color': 'black', 'border': '1px solid blue'},
                                                 style_data_conditional=[{'if': {'row_index': 'odd'}, 'backgroundColor': 'rgb(220, 220, 1500)'}],
                                                 style_table={'height': '85px', 'overflowY': 'auto'}
                                                 ),
                            id=ids.cust_firmo_id)

    return html.Div(id=ids.cust_firmo_id)
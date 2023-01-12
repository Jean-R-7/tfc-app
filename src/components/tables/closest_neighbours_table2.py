from dash import Dash, html, Input, Output, dcc, dash_table,  ctx, State
from src.components.Ids import ids
from src.components.data.load_data import  COLNAMES
import re
import pandas as pd
from src.components.data.data_uploader import parse_data


def render(app: Dash) -> html.Div:
    # data = TFC_output()

    def GetNeighbours(data,neighb_indices, ColName):
        idx = str(set(neighb_indices[ColName].values))
        idx = re.sub("[nan'(){},\[\]]", "", idx).replace(' ', ',').lstrip(',').rstrip(',').split(  ",")  # clean the index cells . rstrip is to remove last comma in string if any, and lstrip is to remove the comma before the string
        if '' in idx:
            idx.remove('')
        idx = list(map(int, idx))
        neighb_indices = data.loc[idx,][COLNAMES.l_col_id + COLNAMES.l_col_firm + COLNAMES.A_count + [COLNAMES.A]]
        if neighb_indices.shape[0] == 0:
            neighb_indices= pd.DataFrame("N/A", index=['1'], columns=neighb_indices.columns)
        return neighb_indices

    @app.callback(
        Output(ids.neighb_firmo_id, 'children'),
        Input(ids.cust_dropdown_id, 'value'),
        Input(ids.strong_btn,'n_clicks'),
        Input(ids.good_btn, 'n_clicks'),
        Input(ids.avg_btn, 'n_clicks'),
        Input(ids.weak_btn, 'n_clicks'),
        State(ids.upload_botton, 'contents'),  # to call the data
        State(ids.upload_botton, 'filename')  # to call the data
    )
    def update_cust_firmo_table(customer: list[str], strong_btn, good_btn, avg_btn,weak_btn, contents, filename) -> html.Div():

        if customer==None:
            return dcc.Textarea(value='Select a customer from above list to display table',style={'color': 'yellow'})

        # call the data-------------------------------------------
        if contents:
            contents = contents[0]
            filename = filename[0]
            data = parse_data(contents, filename)
            neighb_indices = data.query("`Cleaned Parent Customer` in @customer")[  COLNAMES.l_col_firm_indx]  # bring the indices of all types of neighbours
            #---------------

            if ids.strong_btn == ctx.triggered_id:
                df=GetNeighbours(data,neighb_indices, COLNAMES.SF_indx)

            elif ids.good_btn == ctx.triggered_id:
                df=GetNeighbours(data,neighb_indices, COLNAMES.GF_indx)

            elif ids.avg_btn == ctx.triggered_id:
                df=GetNeighbours(data,neighb_indices, COLNAMES.AF_indx)

            elif ids.weak_btn == ctx.triggered_id:
                df=GetNeighbours(data,neighb_indices, COLNAMES.WF_indx)

            else:
                df=GetNeighbours(data,neighb_indices, COLNAMES.SF_indx)


            return html.Div(dash_table.DataTable(data=df.to_dict('records'),
                                             columns=[{"name": i, "id": i} for i in df.columns],
                                             # export_format='csv',
                                             style_cell={'textAlign': 'left'},
                                             style_header={'backgroundColor': 'grey', 'color': 'black', 'fontWeight': 'bold'},
                                             style_data={'backgroundColor': 'white', 'color': 'black', 'border': '1px solid blue'},
                                             style_data_conditional=[{'if': {'row_index': 'odd'}, 'backgroundColor': 'rgb(190, 229, 176)'}],
                                             style_table={'height': '230px', 'overflowY': 'auto'}
                                             ),
                        id=ids.neighb_firmo_id)

    return html.Div(id=ids.neighb_firmo_id)
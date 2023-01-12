import pandas as pd
from dash import Dash
from dash import html, Input, Output, dash_table
import plotly.express as px # there is a datatset in this package
from src.components.Ids import ids



def render(app: Dash) -> html.Div:
    @app.callback(
        Output(ids.table1_id, 'children'),
        Input(ids.all_nations_dropdown_id, 'value')
    )

    def update_table(nations: list[str]) -> html.Div():
        filtered_data=Medal_data().query("nation in @nations")
        # if filtered_data.shape[0]==0:
        #     return html.Div('No Data Selected - Please Upload Data')
        return html.Div(dash_table.DataTable(data=filtered_data.to_dict('records'),
                                             columns=[{"name": i, "id": i} for i in Medal_data().columns],
                                             export_format='csv',
                                             style_cell={'textAlign': 'center'},
                                             style_header={'backgroundColor': 'grey', 'color': 'black', 'fontWeight': 'bold'},
                                             style_data={'backgroundColor': 'white', 'color': 'black', 'border': '1px solid blue'},
                                             style_data_conditional=[{'if': {'row_index': 'odd'}, 'backgroundColor': 'rgb(220, 220, 1500)'}]
                                             ),
                        id=ids.table1_id)

    return html.Div(id=ids.table1_id)




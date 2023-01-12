from dash import Dash, html, Input, Output, dcc, dash_table,  ctx, State
from src.components.Ids import ids
from src.components.data.load_data import  COLNAMES
from src.components.data.data_uploader import parse_data
import dash_bootstrap_components as dbc # for themes
import re
#10G LLC AKA ILDIVOF MOREYCATERP
def render(app: Dash) -> html.Div:

    @app.callback(
        Output(ids.recom_boxes, 'children'),
        Input(ids.cust_dropdown_id, 'value'),
        State(ids.upload_botton, 'contents'), # to call the data
        State(ids.upload_botton, 'filename') # to call the data
    )
    def update_recom_box(customer: list[str], contents,filename) -> html.Div():
        if customer==None:
            return dcc.Textarea(value='Please select a customer', style={'color': 'red'})

    # call the data-------------------------------------------
        if contents:
            contents = contents[0]
            filename = filename[0]
            data = parse_data(contents, filename)
    # --------------------------------------------

            DF = data.query("`Cleaned Parent Customer` in @customer")

            return html.Div(dbc.Container([
            # Customer recommendations
                            dbc.Row([
                                dbc.Col([
                                    html.H6('Current Portfolios'),
                                    html.Div([dcc.Textarea(
                                                           value=','.join(DF[COLNAMES.A].fillna('')),
                                                           style={'height': '100px', 'overflow': 'auto'}),
                                              dbc.Button(re.sub(r'[^\w]', "",str(DF[COLNAMES.A_count].values)), color="light")
                                              ])], width=2),

                                dbc.Col([
                                    html.H6('Strong Recommendations'),
                                    html.Div([dcc.Textarea(
                                                           value=','.join(DF[COLNAMES.S_recom].fillna('')),
                                                           style={'height': '100px', 'overflow': 'auto'}),
                                             dbc.Button(re.sub(r'[^\w]', "",str(DF[COLNAMES.S_recom_count].values)), color="success")
                                              ])], width=2),

                                dbc.Col([
                                    html.H6('Good Recommendations'),
                                    html.Div([dcc.Textarea(
                                                           value=','.join(DF[COLNAMES.G_recom].fillna('')),
                                                           style={'height': '100px', 'overflow': 'auto'}),
                                            dbc.Button(re.sub(r'[^\w]', "",str(DF[COLNAMES.G_recom_count].values)), color="primary")
                                              ])], width=2),

                                dbc.Col([
                                    html.H6('Average Recommendations'),
                                    html.Div([dcc.Textarea(
                                                           value=','.join(DF[COLNAMES.A_recom].fillna('')),
                                                           style={'height': '100px', 'overflow': 'auto'}),
                                             dbc.Button(re.sub(r'[^\w]', "",str(DF[COLNAMES.A_recom_count].values)), color="warning")
                                              ])], width=2),

                                dbc.Col([
                                    html.H6('Weak Recommendations'),
                                    html.Div([dcc.Textarea(
                                                           value=','.join(DF[COLNAMES.W_recom].fillna('')),
                                                           style={'height': '100px', 'overflow': 'auto'}),
                                            dbc.Button(re.sub(r'[^\w]', "",str(DF[COLNAMES.W_recom_count].values)), color="danger")
                                              ])], width=2),

                            ], justify='center')

                                    ]),  # for container
                        id=ids.recom_boxes)#for html.Div

    return html.Div(id=ids.recom_boxes)
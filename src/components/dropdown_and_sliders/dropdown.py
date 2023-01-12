
from dash import Dash, html,  Input, Output, dcc, State, dash_table
from src.components.Ids import ids
from src.components.data.load_data import COLNAMES
from src.components.data.data_uploader import parse_data

def render(app: Dash) -> html.Div:

    @app.callback(
        Output(ids.cust_dropdown_id, 'children'),
        Input(ids.upload_botton, 'contents'),
        State(ids.upload_botton, 'filename')
    )
    def update_dropdown(contents, filename):
        if contents:
            contents = contents[0]
            filename = filename[0]
            df = parse_data(contents, filename)
                   #html.Div([html.H6("The file, " + '"{}"'.format(filename) + ' has been uploaded'),
            return dcc.Dropdown(id=ids.cust_dropdown_id,
                                          options=[{'label': customer, 'value': customer} for customer in df['Cleaned Parent Customer'].unique()],  # ['1A CAL', '3 PHOENIX', '1ST DETECT']
                                          style={'color': 'black', 'background-color': 'cyan'},
                                          value="1A CAL", multi=False)
                             # ])

            # return html.Div([html.H6("The file, " + '"{}"'.format(filename) + ' has been uploaded'),
            #                           dash_table.DataTable(
            #                                 data=df.to_dict('rows'),
            #                                 style_data={'backgroundColor': 'white', 'color': 'black'},
            #                                 columns=[{'name': i, 'id': i} for i in df.columns]
            #                                  ),
            #             html.Hr()  # horizontal line
            #                    ])

    return html.Div(id=ids.cust_dropdown_id)

# def render(app: Dash) -> html.Div:
#     df = TFC_output()
#
#     return html.Div([dcc.Dropdown(id=ids.cust_dropdown_id,
#                                   options=[{'label': customer, 'value': customer} for customer in ['1A CAL', '3 PHOENIX','1ST DETECT']],
#                                   style={'color': 'black', 'background-color': 'rgb(40,40,40)'},
#                                   value=[], multi=True)])
# #

from dash import Dash
from dash import dcc, html, Input, Output, State, dash_table
import io
import base64
import datetime
import pandas as pd

import dash_bootstrap_components as dbc # for themes

from src.components.Ids import ids
# from src.graphs import bar_chart, scatter_plot
from src.components.tables import customer_firmo_table, recommendations, closest_neighbours_table1,  closest_neighbours_table2
from src.components.dropdown_and_sliders import dropdown, button_upload

# #
from PIL import Image
pil_image = Image.open("components/logo/analog_logo.png")

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY]) #other themes are found here https://towardsdatascience.com/3-easy-ways-to-make-your-dash-application-look-better-3e4cfefaf772

server=app.server
############ layout
app.layout = html.Div(className='app-div',children=[

    dbc.Container([
### titles and subtitles
        dbc.Row([html.Hr(),
                 dbc.Col([html.H3(children='TFC Model App',  style={"text-align": "left"}) ]),
                 dbc.Col([html.Div(html.Img(src=pil_image,style={'height':'15%', 'width':'15%'}),style={'textAlign': 'right'}) ]),
                 html.Hr()
                 ],justify='center'),


#### customer dropdown
        dbc.Row([
            dbc.Col([
                button_upload.render(app),
                # data_uploader.render(app),
                html.Hr(),
                html.Div([ dropdown.render(app)]),

            ],width=3),
                # html.H6(children='Select/Type Customer Name'),
                ],justify='left'), #

        html.Hr(),

        dbc.Row([
            dbc.Col([html.H5(children="Customer's Firmographics:")], width=6)
        ], justify='left'),
#
#         ### customer's Firmo
        dbc.Row([
            dbc.Col([customer_firmo_table.render(app)],
                    width=12),
                ], justify='center'),
#
       html.Br()
        ]),
#
    dbc.Container([
    # Customer recommendations

        recommendations.render(app),
     html.Hr(),

    ]),
#
#
#
# ### neighbours' Firmo
    dbc.Container([

        dbc.Row([
            dbc.Col([html.H5(children="Closest Neighbours' Firmographics and Portfolios:"),
                     html.Br(),
                     html.H6(children="Choose Neighbour type to display table:")
                     ],width=6)
        ],justify='left'),
        ]),
#
    dbc.Container([
        dbc.Row([
             dbc.Col([dbc.Button('Strong Neighbours', id=ids.strong_btn, n_clicks=0, color='success')],width=2),
             dbc.Col([dbc.Button('Good Neighbours', id=ids.good_btn, n_clicks=0,color='primary')],width=2),
             dbc.Col([dbc.Button('Average Neighbours', id=ids.avg_btn, n_clicks=0,color='warning')],width=2),
             dbc.Col([dbc.Button('Weak Neighbours', id=ids.weak_btn, n_clicks=0,color='danger')],width=2),

        ], justify='center'),

      html.Br(),
#
         dbc.Row([
            dbc.Col([
                     html.Div('Portfolio Neighbours'),
                     html.Div(closest_neighbours_table1.render(app)),
                     html.Br(),
                     html.Div('Firmographic Neighbours'),
                     html.Div(closest_neighbours_table2.render(app))
                     ],
                    width=12)

        ], justify='center')


]), # For container

 ] ) # for html.div

###############################  to upload data. The output will be located where the ùpload buttoon is located is located


# def render(app: Dash) -> html.Div:

# @app.callback(Output(ids.output_data_upload, 'children'),
#               Input(ids.upload_botton, 'contents'),
#               State(ids.upload_botton, 'filename'))
#               # State(ids.upload_botton, 'last_modified'))
#
# def update_output(contents, filename):
#     if contents:
#         contents = contents[0]
#         filename = filename[0]
#         df=data_uploader.parse_data(contents, filename)
#         # df = df.set_index(df.columns[0])
#         # df = parse_data(contents, filename)
#         return html.Div([ html.H6("The file, " + '"{}"'.format(filename) + ' has been uploaded'),
#                           dash_table.DataTable(
#                                 data=df.to_dict('records'),
#                                 style_data={'backgroundColor': 'white', 'color': 'black'},
#                                 columns=[{'name': i, 'id': i} for i in df.columns]
#                                  ),
#             html.Hr()  # horizontal line
#                    ])
#########################################################################################



if __name__ == '__main__':
    app.run_server(debug=True)




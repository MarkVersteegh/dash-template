# TAB_CONTENTS.PY - Contains code setting the layout of the app's tabs

from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

import layout.table_contents as tblc # Refers to table_contents.py which holds code dealing with tables to be displayed

# Content of tab 1
tab1_content = dbc.Row([
    dbc.Col(
        html.Div([
            html.H6('Checklist with options'),
            dcc.Checklist(
                id='test-checkbox'
                , options=[]
                , value=[]
            )
        ])
    , width=3),
    dbc.Col(
        html.Img(src=r'assets/OGD prompt RGB.png', alt='image', style={'maxHeight': '400px', 'maxWidth': '400px'})  # You can save an image in the assets folder and display it here
    , width=3),
    dbc.Col(
        html.Div([
            dbc.Button(
                'Just a cool button'
                , id='cool-button-1'
                , n_clicks=0
                , color='primary'
                , className='btn btn1'
            ),
            dbc.Button(     # Button is used to toggle save data button (save-button)
                'Toggle save button'
                , id='cool-button-2'
                , n_clicks=0
                , color='primary'
                , className='btn btn2'
            ),
            dbc.Button(
                'Another cool button'
                , id='cool-button-3'
                , n_clicks=0
                , color='primary'
                , className='btn btn3'
            )
        ], style={'display': 'grid'})
    , width=6)
])

# Content of tab 2
tab2_content = dbc.Row([ # A row is a horizontal layout element from dash bootstrap
    dbc.Col( # A column is a vertical layout element from dash bootstrap
        html.Div([
            html.H3('This is a very loooooooooooooooooooooooooooooooooooooooooooooooooooooooonggggggggg text')
        ])
    , width=8), # The width of a column can be set here. The entire width of an app is 12
    dbc.Col(
        html.Div([
            tblc.data_table # Refers to a data table from table_contents.py
        ], id='data-table-div', style={'width': '15%', 'margin-top': '1%', 'display': 'inline-block'})
    , width=4)
])

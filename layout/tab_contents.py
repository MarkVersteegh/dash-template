# TAB_CONTENTS.PY - Contains code setting the layout of the app's tabs

from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

import layout.table_contents as tblc # Refers to table_contents.py which holds code dealing with tables to be displayed

# Content of tab 1
tab1_content = dbc.Row([ # A row is a horizontal layout element from dash bootstrap
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

# Content of tab 2
tab2_content = dbc.Row([
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
        html.Div([
        ])
    , width=3),
    dbc.Col(
        html.Div([
        ])
    , width=3),
    dbc.Col(
        html.Div([
        ])
    , width=3)
])

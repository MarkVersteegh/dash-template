from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

import layout.tab_contents as tc # Refers to tab content from tab_contents.py which is also in the layout folder

# Main layout
layout = dbc.Row([ # A row is a horizontal layout element from dash bootstrap
    html.H1('Title (in OGD-huisstijl!)', id='title', style={'color': '#000000'}),
    dcc.Store(id='data-store'), # dcc.Store can hold data, but it needs to be stored in JSON format
    dbc.Input(
        type='text'
        , id='basic-text-input' # id is the unique identifier for a Dash element
        , placeholder='Enter some Hello World-like text'
    ),
    dbc.Button( # Bootstrap button, which is quite similar to the generic Dash button
        'Save entered value to data table on Tab 2'
        , id='save-button'
        , n_clicks=0
        , disabled=False
        , color='primary'
        , style={'width': '49%', 'margin-left': '1%', 'margin-bottom': '1%'}
    ),
    dbc.Tabs([
        dbc.Tab(tc.tab1_content, label='Tab 1', tab_id='tab-1'),
            # Layout elements can be nested from other scrips with code as happened here with tab content
        dbc.Tab(tc.tab2_content, label='Tab 2', tab_id='tab-2')
    ], id='tabs', active_tab='tab-1'),
    html.Div([ # Non-table invisible elements, which can be used to hold tracker values invisible to the user
        dcc.Input(
            id='placeholder'
            , value= 0
        ),
        dcc.Input(
            id='refresh_count'
            , value= 0
        )
    ], style={'display': 'none'}) # Style elements can be used to set both appearance and visibility
], style={'margin': '1%'})
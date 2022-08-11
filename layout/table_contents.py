# TABLE_CONTENTS.PY - Contains code to create tables displaying data

from dash import dash_table

data_table = dash_table.DataTable(
    id='data-table',
    columns=[], # Specifies the table's columns, empty for now as it will be set using a callback function
    data=[], # Specifies the table's columns, empty for now as it will be set using a callback function
    fixed_rows={'headers': True }, # Headers will appear at the top of the table, even when scrolling
    style_table={   # CSS style parameters, which affect the table's appearance
        'minHeight': '11vh'
        , 'height': '11vh'
        , 'maxHeight': '11vh'
        , 'overflow-y': 'scroll'
        , 'border': '1.5px solid #000000'
        , 'color': '#000000'
        , 'font-size': '15px'
        , 'display': 'inline-block'
    },
    style_cell={    # Affects formatting of the table's cells
        'textAlign': 'left'
        , 'font-family': 'Arial'
    },
    style_header={  # Affects the styling of table headers
        'fontWeight': 'bold'
        , 'whiteSpace': 'normal'
        , 'height': 'auto'
    },
    style_data={
        'whiteSpace': 'normal'
        , 'height': 'auto'
    },
    style_cell_conditional=[    # Conditional styling can be applied, like setting column width conditional on column name
        {'if': {'column_id': 'Hello World'},
         'width': '100%'}
    ]
)
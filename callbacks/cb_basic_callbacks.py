# cb_basic-callbacks is an example of a file containing callback functions
# Callback functions are called when an element from the layout is altered, clicked or filled in
# A callback function consists of one or more outputs, inputs, or states
# Outputs are the results of the callback, such altering an element's properties
# Inputs are elements that trigger a callback
# States are other elements imported into the callback, but these do not trigger the callback
# Each Dash element in the app may only once be used as a callback output

# Import Python Dash modules for callbacks
from dash.dependencies import Input, Output, State  # These Dash dependencies contain the main elements of callback functions
from dash import callback_context   # Module that can determine which element triggered a callback, handy for determining a workflow based on the triggering element

# Import modules for working with data
import pandas as pd
import functions.data_construction as dc


def register_cb_basic_callbacks(app):
    @app.callback(  # This callback will provide options to the checkbox on tab 2
        Output('test-checkbox', 'options'),
        Input('placeholder', 'value')
    )
    def set_checkbox_options(
        placeholder
    ):
        # Get the callback context and derive the triggering element from it
        ctx = callback_context
        trigger_element = ctx.triggered[0]['prop_id']

        checkbox_options = pd.DataFrame({"option": ['Ja', 'Nee'], "sort": [1, 2]})
        checkbox_options = dc.construct_options(
            df=checkbox_options
            , value_column='option'
            , label_columns=['option'] # Must be entered as list of columns
            , sort_column='sort'
            , concat_separator='' # Used as a concatenator for multi-column labels
        )

        return checkbox_options


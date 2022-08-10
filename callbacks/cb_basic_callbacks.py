# cb_basic-callbacks is an example of a file containing callback functions
# Callback functions are called when an element from the layout is altered, clicked or filled in
# A callback function consists of one or more outputs, inputs, or states
# Outputs are the results of the callback, such altering an element's properties
# Inputs are elements that trigger a callback
# States are other elements imported into the callback, but these do not trigger the callback

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

    @app.callback(  # This callback will use the Hello World input in a dataframe which is then saved into a dcc.Store
        Output('data-store', 'data'),
        Input('save-button', 'n_clicks'),   # Clicking the save button will trigger the callback
        State('basic-text-input', 'value')  # Typing a text into the input box will not trigger the callback, but will provide a value for further processing
    )
    def set_hello_world_df(
        save_button_n_clicks
        , basic_text_input
    ):
        # Create a basic Hello World dataframe from inputs
        df = pd.DataFrame({"Hello World": [basic_text_input]})
        df = dc.save_df_into_store(df=df)

        return df

    @app.callback(  # This callback will use the Hello World dataframe from the dcc.Store and put it into display table
        Output('data-table', 'columns'),
        Output('data-table', 'data'),
        Input('data-store', 'data'),
    )
    def display_hello_world_df(
        data_stored
    ):
        # Load dataframe from data store
        df = dc.load_df_from_store(store_df=data_stored)

        # Convert retrieved data frame into columns and data
        columns = [{"name": i, "id": i} for i in df.columns]
        data = df.to_dict('records')

        # Return population allocation data
        return columns, data

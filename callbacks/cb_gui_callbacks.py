# Import Python Dash modules for callbacks
from dash.dependencies import Input, Output, State  # These Dash dependencies contain the main elements of callback functions
from dash import callback_context   # Module that can determine which element triggered a callback, handy for determining a workflow based on the triggering element


def register_cb_gui_callbacks(app):
    @app.callback(  # This callback will activate tab 1 upon clicking the save button
        Output('tabs', 'active_tab'),
        Input('save-button', 'n_clicks')
    )
    def activate_tab1_on_hitting_save_button(
        save_button_n_clicks
    ):
        if save_button_n_clicks > 0:
            return 'tab-1'
        else:
            return 'tab-2'

    @app.callback(  # This callback will toggle availability of the save button upon clicking cool button 2
        Output('save-button', 'disabled'),
        Input('cool-button-2', 'n_clicks'),
        State('save-button', 'disabled')    # Note that an output can be used as a state at the same time
    )
    def toggle_save_button_availability(
        cool_button_2_n_clicks
        , save_button_disabled
    ):
        if save_button_disabled:
            return False
        else:
            return True

    @app.callback(  # This callback will alter the title's colour according to that of the button being clicked
        Output('title', 'style'),
        Input('tabs', 'active_tab'),
        Input('cool-button-1', 'n_clicks'),
        Input('cool-button-2', 'n_clicks'),
        Input('cool-button-3', 'n_clicks')
    )
    def change_title_colour(
        tabs_active_tab
        , cool_button_1_n_clicks
        , cool_button_2_n_clicks
        , cool_button_3_n_clicks
    ):
        # Get the callback context and derive the triggering element from it
        ctx = callback_context
        trigger_element = ctx.triggered[0]['prop_id']

        # The code below demonstrates how trigger context can be used to trigger different actions based on trigger context

        colour = '#000000'   # Set black as the title's default colour

        if trigger_element == 'cool-button-1.n_clicks':
            colour = '#043673'
        elif trigger_element == 'cool-button-2.n_clicks':
            colour = '#e2241d'
        elif trigger_element == 'cool-button-3.n_clicks':
            colour = '#37cfb1'

        colour_style = {'color': colour}

        return colour_style

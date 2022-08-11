# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# Import basic dash module
import dash
import dash_bootstrap_components as dbc

# Import app layout
from layout.layout import layout

# Import callback functions
from callbacks.cb_basic_callbacks import register_cb_basic_callbacks
from callbacks.cb_gui_callbacks import register_cb_gui_callbacks
    # Reference to the script with callback functions, importing the wrapper function containing the callback functions

# Initialise app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    # The app itself is defined here, along with its formatting/style
    # The styling comes from an external stylesheets, which can be custom as well!
app.config.suppress_callback_exceptions=True

# Initialise app layout
app.layout = layout

# Initialise callbacks
register_cb_basic_callbacks(app=app)    # The app itself must be passed to the wrapper callback function
register_cb_gui_callbacks(app=app)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

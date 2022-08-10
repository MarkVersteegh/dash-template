# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# Import basic dash module
import dash
import dash_bootstrap_components as dbc

# Import app layout
from layout.layout import layout

# Initialise app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config.suppress_callback_exceptions=True

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

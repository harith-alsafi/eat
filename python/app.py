from constant import APP_NAME
import dash
import dash_bootstrap_components as dbc

app = dash.Dash(
    APP_NAME, 
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        dbc.icons.BOOTSTRAP,
    ],
)
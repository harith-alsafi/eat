from constant import APP_NAME
import dash
import dash_bootstrap_components as dbc
external_stylesheets = [dbc.themes.BOOTSTRAP,
                        'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css',
                        dbc.icons.BOOTSTRAP]

app = dash.Dash(
    APP_NAME, 
    external_stylesheets=external_stylesheets
)
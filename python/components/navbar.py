from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app

def nav_bar():
    layout = dbc.Navbar(
        dbc.Container(
            [
            
            ]
        ),
        color="dark",
        dark=True,
    )

    return layout
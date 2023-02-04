from dash import html
import dash_bootstrap_components as dbc

def build():
    print("build home")
    return dbc.Container(
        [
        dbc.Row([
            html.Center(html.H1("Home")),
        ])
        ]
    )
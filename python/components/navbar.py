from dash import html
import dash_bootstrap_components as dbc

def nav_bar():
    layout = html.Div([
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("Logout", href="/logout")),
            ] ,
            brand="EAT Dashboard",
            brand_href="/home",
            color="dark",
            dark=True,
        ),
    ])

    return layout

from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app
from dash_iconify import DashIconify

MAIN_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

logo = dbc.Row(
    [
        dbc.Col(html.Img(src=MAIN_LOGO, height="30px"), width={"order":0}),
        dbc.Col(dbc.NavbarBrand("1Eat", className="ms-2"), width={"order":1}),
    ],
    align="left",
    className="g-0",
)


switchers = dbc.Row(
    [
        dbc.Col(dbc.Button("Overview")),
        dbc.Col(dbc.Label(" | ")),
        dbc.Col(dbc.Button("Details")),
    ],
    align="left",
    className="g-0",
)

buttons = dbc.Row(
    [
        dbc.Col(DashIconify(
        icon="ic:outline-account-circle",
        width=30,
        color="white"
    )),
          dbc.Col(width=20),
        dbc.Col(DashIconify(
                icon="ant-design:setting-outlined",
                width=30,
                color="white" 
            ),
            width="auto",
        ),
    ],
    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.Col(logo, align="left", width="auto"),
            dbc.Col(switchers, align="center", width="auto"),
            dbc.Col(buttons,align="right", width="auto"),
        ]
    ),
    color="dark",
    dark=True,
)
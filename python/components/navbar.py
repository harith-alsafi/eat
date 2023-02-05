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

# add callback for toggling the collapse on small screens
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
    # print("build navbar")
    # return dbc.Navbar(
    #         dbc.Row(
    #             # dbc.Col(
    #             [
    #                 # dbc.Label(
    #                 #     html.I(className="bi bi-1-square-fill"),
    #                 #     className="g-0",
    #                 #     # href="/home",
    #                 # ),
          
    #                         dbc.Col(dbc.Label("Overview", align="start"), width={"size": 3, "order": 1}),
    #                         dbc.Col(dbc.Label(" | ", align="center"), width={"size": 3, "order": 2}),
    #                         dbc.Col(dbc.Label("Detailed", align="end"), width={"size": 3, "order": 4, "offset": 1}),
              
    #                         dbc.Col(dbc.Label(html.I(className="bi bi-person-circle")), width={"size": 3, "order": 5, "offset": 1}),
    #                         dbc.Col(dbc.Label(html.I(className="bi bi-gear")), width={"size": 3, "order": 6, "offset": 1})
                 
    #             ],
    #             # )
    #         ),
    #     )
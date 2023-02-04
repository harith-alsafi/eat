from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app

def nav_bar():
    print("build navbar")
    return dbc.Navbar(
            dbc.Row(
                # dbc.Col(
                [
                    # dbc.Label(
                    #     html.I(className="bi bi-1-square-fill"),
                    #     className="g-0",
                    #     # href="/home",
                    # ),
          
                            dbc.Col(dbc.Label("Overview", align="start"), width={"size": 3, "order": 1}),
                            dbc.Col(dbc.Label(" | ", align="center"), width={"size": 3, "order": 2}),
                            dbc.Col(dbc.Label("Detailed", align="end"), width={"size": 3, "order": 4, "offset": 1}),
              
                            dbc.Col(dbc.Label(html.I(className="bi bi-person-circle")), width={"size": 3, "order": 5, "offset": 1}),
                            dbc.Col(dbc.Label(html.I(className="bi bi-gear")), width={"size": 3, "order": 6, "offset": 1})
                 
                ],
                # )
            ),
        )
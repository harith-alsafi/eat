import dash_bootstrap_components as dbc
from dash import html, dcc
import plotly.express as px
import numpy
from dash.dependencies import Input, Output
from app import app
from dash_iconify import DashIconify


def Get_Card(title, numberChange, percentChange, period, expectedPercent):
    periodText = f"{period} month"
    if period != 1:
        periodText = f"{periodText}s"

    percentChangeColour = "text-success" if percentChange > 0 else "text-danger"
    expectedPercentColour = "text-success" if expectedPercent > 0 else "text-danger"

    return dbc.Card([
        dbc.CardBody(
            [
                html.H5(title, className="card-title text-secondary"),

                html.H3(numberChange, className="card-text-change d-flex justify-content-center"),
                # dbc.Row([
                #     dbc.Col(html.H3(f"${numberChange:,.2f}", className="card-text-change d-flex justify-content-center")),
                #     dbc.Col(DashIconify(
                #         icon=("material-symbols:arrow-drop-up" if percentChange > 0 else "material-symbols:arrow-drop-down"),
                #         color=("green" if percentChange > 0 else "red"),
                #         height=30,
                #         width=30
                #     ))
                # ], align="center"),

                html.P(f"{percentChange/100:.0%}", className=f"card-text-change-percent d-flex justify-content-center {percentChangeColour}"),
                html.P(f"from last {periodText}", className="card-text-period d-flex justify-content-center text-secondary"),
                html.P(f"{expectedPercent/100:.0%} expected next month", className=f"card-text-expected d-flex justify-content-center {expectedPercentColour}"),
            ]
        ),
    ],
    style={"height":"100%"}
)

def Get_overview():

    return dbc.Col(
        [
        dbc.Row([
            dbc.Col(Get_Card("Profit", "24037$", 25, 1, 32)),
            dbc.Col(Get_Card("EC/Revenue", 0.45, 2.5, 1, -1.2)),
            dbc.Col(Get_Card("Carbon Credit", 103, 2.5, 1, -3.2)),
        ], style={"height":"44vh",'margin': 10 }),
        dbc.Row([
            dbc.Col(dbc.Card(dbc.CardBody(dbc.Row(dcc.Graph(figure=generate_chart()) , align = "center"))), width="8", align="center"),
            dbc.Col(Get_Card("Carbon Emission", "23403 tonnes", 2.5, 1, 3.2), width="4"),
        ], style={"height":"44vh", 'margin': 10 }, class_name="display: flex; flex-grow: 1;")
        ],
        width="100%",
        style={"height":"100%"}
    )


def generate_chart():
    random_x = [100, 2000, 550, 100, 1233]
    names = ['Enviromental costs', 'Workforce costs', 'Logistics costs', 'Other costs', 'Profits']
    fig = px.pie(values=random_x, names=names, height=400, width=1000)
    return fig
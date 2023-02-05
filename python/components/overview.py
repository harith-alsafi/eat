import dash_bootstrap_components as dbc
from dash import html, dcc
import plotly.express as px
import numpy
from dash.dependencies import Input, Output
from app import app


def Get_Card(title, numberChange, percentChange, period, expectedPercent):
    return dbc.Card([
        dbc.CardBody(
            [
                html.H2(title, className="card-title"),
                html.P(str(numberChange), className="card-text-change"),
                html.P(str(percentChange)+"%", className="card-text-change-percent"),
                html.P(str(period), className="card-text-period"),
                html.P(str(expectedPercent)+"%", className="card-text-expected"),
            ]
        ),
    ],
    style={"height":"100%"}
)

def Get_overview():

    return dbc.Col(
        [
        dbc.Row([
            dbc.Col(Get_Card("1Profit", 23403, 2.5, 1, 3.2)),
            dbc.Col(Get_Card("2Profit", 23403, 2.5, 1, 3.2)),
            dbc.Col(Get_Card("3Profit", 23403, 2.5, 1, 3.2)),
        ], style={"height":"44vh",'margin': 10 }),
        dbc.Row([
            dbc.Col(dbc.Card(dbc.CardBody(dbc.Row(dcc.Graph(figure=generate_chart()) , align = "center"))), width="8", align="center"),
            dbc.Col(Get_Card("5Profit", 23403, 2.5, 1, 3.2), width="4"),
        ], style={"height":"44vh", 'margin': 10 }, class_name="display: flex; flex-grow: 1;")
        ],
        width="100%",
        style={"height":"100%"}
    )


def generate_chart():
    random_x = [100, 2000, 550]
    names = ['A', 'B', 'C']
    fig = px.pie(values=random_x, names=names, height=400, width=1000)
    return fig
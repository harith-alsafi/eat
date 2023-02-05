import dash_bootstrap_components as dbc
from dash import html, dcc
import plotly.express as px
import numpy
from dash.dependencies import Input, Output
from app import app
# import table

def Get_Details():

    return dbc.Col(
        [
        dbc.Row([
            dbc.Col(),
            dbc.Col(),
        ], style={"height":"44vh",'margin': 10 }),
        dbc.Row([
            dbc.Col(),
            # dbc.Col(table.old_table_view),
        ], style={"height":"44vh", 'margin': 10 }, class_name="display: flex; flex-grow: 1;")
        ],
        width="100%",
        style={"height":"100%"}
    )
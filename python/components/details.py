import dash_bootstrap_components as dbc
from dash import html, dcc
import plotly.express as px
import numpy
from dash.dependencies import Input, Output
from app import app
from . import table
import pandas as pd
import dash_daq as daq

random_temperature = 18

def Get_Details():
    return dbc.Col(
        [
        dbc.Row([
            dbc.Col(dbc.Card(dbc.CardBody(dbc.Row(Get_progress(), align = "center")), style={'height':'43.4vh'})),
            dbc.Col(dbc.Card(dbc.CardBody(dbc.Row( dcc.Graph(figure=Get_map()),align = "center")))),
        ], style={"height":"44vh",'margin': 10 }),
        dbc.Row([
            dbc.Col(dbc.Card(dbc.CardBody(dbc.Row(dcc.Graph(figure=Get_3d()) , align = "center")))),
            dbc.Col(dbc.Card(dbc.CardBody(dbc.Row(dcc.Graph(figure=Get_TimeLine()), align = "center")))),
        ], style={"height":"44vh", 'margin': 10 }, class_name="display: flex; flex-grow: 1;"),
        dbc.Row([
            dbc.Col(table.old_table_view),
        ], style={"height":"44vh", 'margin': 10 }, class_name="display: flex; flex-grow: 1;")
        ],
        width="100%",
        style={"height":"100%"}
    )

def Get_progress():
    return     daq.Gauge(
        id='Performance',
        label="Performance",
        value=12,
        min=0,
        max=100,
        showCurrentValue=True,
        units="%",
        style={"height":"400vh"}
    ),

def Get_TimeLine():
        # Get some data
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

    # Plot 
    fig = px.line(df, x='Date', y='AAPL.High', height=380, title="Emission")
    fig.update_layout(
    yaxis_title="CO2 metric tonne",
)

    # Only thing I figured is - I could do this 
    fig.add_scatter(x=df['Date'], y=df['AAPL.Low'], mode='lines')
    return fig

def Get_3d():
    df = px.data.gapminder().query("continent=='Europe'")
    fig = px.line_3d(df, x="gdpPercap", y="pop", z="year", color='country', height=380)
    fig.update_layout(
        title="Emissions",
        )
    return fig

def Get_map():
    data=[[1, 25, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, 5, 20]]
    fig = px.imshow(data,
                    labels=dict(x="Day of Week", y="Time of Day", color="Productivity"),
                    x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                    y=['Morning', 'Afternoon', 'Evening']
                , height=380)
    fig.update_xaxes(side="top")
    return fig
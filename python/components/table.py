import pandas as pd
import dash_bootstrap_components as dbc
import os

if os.name == 'nt':
    matlab_data = pd.read_csv("eat\matlab\hello.csv")
else:
    matlab_data = pd.read_csv('matlab/hello.csv')
old_table_view = dbc.Table.from_dataframe(matlab_data, striped=True, bordered=True, hover=True)
import pandas as pd
import dash_bootstrap_components as dbc
import os

if os.name == 'nt':
    matlab_data = pd.read_csv("eat\matlab\data.csv")
else:
    matlab_data = pd.read_csv('../matlab/data.csv')
old_table_view = dbc.Table.from_dataframe(matlab_data, striped=True, bordered=True, hover=True)
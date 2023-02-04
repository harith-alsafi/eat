from dash import html, dcc
from dash.dependencies import Input, Output

from app import app
from pages import home
from components import navbar

nav = navbar.nav_bar()

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    nav,
    html.Div(id='page-content'),
])

@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    match pathname:
        case "/" | "/home":
            return home.layout
        case _:
            return "404"

if __name__ == '__main__':
    from sys import argv
    RUN_AS_DEBUG = "debug" in argv

    app.run_server(debug=RUN_AS_DEBUG)

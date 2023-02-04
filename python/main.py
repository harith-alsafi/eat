from dash import Dash, html

app = Dash("EAT")
app.layout = html.Div([
    html.H1("Hello, World!"),
])

if __name__ == "__main__":
    from sys import argv

    RUN_DEBUG = "debug" in argv
    app.run(debug=RUN_DEBUG)

from dash import html, dcc
from dash.dependencies import Input, Output
from os import environ as env
from urllib.parse import quote_plus, urlencode

from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from flask import session

from app import app
from components import navbar
from components import table
from pages import home as home_page
from components import overview
from components import details
from constant import HOSTNAME


ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

app.server.secret_key = env.get("APP_SECRET_KEY")
oauth = OAuth(app)

oauth.register(
    "auth0",
    client_id=env.get("AUTH0_CLIENT_ID"),
    client_secret=env.get("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration',
)

app.layout = html.Div([
    dcc.Location(id='url'),
    html.Div(id="nav-bar"),
    navbar.navbar,
    overview.Get_overview(),
    # details.Get_Details(),
    html.Div(id='page-content'),
])

@app.server.route("/home")
def home():
    if "user" not in session:
        return app.server.redirect("/login")
    else:
        print(session["user"])
        return ""

@app.server.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    return app.server.redirect("/home")

@app.server.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=f"{HOSTNAME}/callback"
    )

@app.server.route("/logout")
def logout():
    session.clear()
    return app.server.redirect("https://"
        + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": f"{HOSTNAME}/home",
                "client_id": env.get("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        ))

if __name__ == '__main__':
    from sys import argv
    RUN_AS_DEBUG = "debug" in argv

    app.run_server(debug=RUN_AS_DEBUG, port=3000)
    #app.run_server(debug=RUN_AS_DEBUG)

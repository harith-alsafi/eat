from dash import html, dcc
from dash.dependencies import Input, Output
from os import environ as env
from urllib.parse import quote_plus, urlencode

from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv

from app import app
from pages import home
from components import navbar


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

nav = navbar.nav_bar()

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    nav,
    html.Div(id='page-content'),
])

@app.server.route("/")
def home_page():
    print("home")

@app.server.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    app.server.session["user"] = token
    return app.server.redirect("/")


@app.server.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=app.server.url_for("callback", _external=True)
    )


@app.server.route("/logout")
def logout():
    app.server.session.clear()
    app.server.redirect("https://"
        + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": app.server.url_for("home", _external=True),
                "client_id": env.get("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        ))

if __name__ == '__main__':
    from sys import argv
    RUN_AS_DEBUG = "debug" in argv

    app.run_server(debug=RUN_AS_DEBUG)

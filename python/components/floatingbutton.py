from dash import html

button = html.Div(
    [
        html.Button(
            [
                html.I(className="fa-solid fa-plus"),
                html.Span("Test Text", className="visually-hidden"),
            ],
            className="btn btn-success btn-lg dropdown-toggle hide-toggle",
            **{
                "data-bs-toggle":"dropdown",
                "aria-expanded":"false",
                "aria-haspopup":"true",
            }
        ),
        html.Ul(
            [
                html.Li("...", className="dropdown-item"),
            ],
            className="dropdown-menu"
        ),
    ],
    className="dropup position-absolute bottom-0 end-0 rounded-circle m-5"
)

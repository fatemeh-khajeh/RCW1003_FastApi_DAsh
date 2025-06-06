import dash
from dash import html, dcc

app = dash.Dash(
    __name__,
    requests_pathname_prefix="/dashboard/"
)

app.layout = html.Div([
    html.Div([
        html.A('Accueil', href='/')
    ], style={'marginTop': 25}),
    
    dcc.Graph(
        id="exmpl-1",
        figure={
            "data": [
                {"x": [2, 5, 7], "y": [8, 3, 9], "type": "bar", "name": "exmp1"},
                {"x": [5, 3, 8], "y": [6, 2, 5], "type": "bar", "name": "exmp2"}
            ]
        }
    )
])

server = app.server

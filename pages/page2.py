from dash import html, register_page, dcc, callback
from dash.dependencies import Input, Output

register_page(__name__, name='Page 2')

opt = ["oui", "non"]

layout = html.Div([

    html.H1("Aimez-vous Brawl Star:"),

    dcc.RadioItems(id='radio', options=opt, value=None),

    html.P(id='out')

])

@callback(
    Output('out', 'children'),
    Input('radio', 'value')
)
def update(value):
    if value is None:
        txt = "Aucun choix n'a encore été sélectionné."
    elif value == "oui":
        txt = "Génial, jouons ensemble !"
    else:
        txt = "Dommage, réflechis encore"
    return txt
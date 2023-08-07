from dash import Dash, html, dcc, callback, Output, Input
import dash_daq as daq
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go


# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')
fig = go.Figure()

fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = 200,
    domain = {'x': [0, 0.5], 'y': [0, 0.5]},
    delta = {'reference': 400, 'relative': True, 'position' : "top"}))

fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = 350,
    delta = {'reference': 400, 'relative': True},
    domain = {'x': [0, 0.5], 'y': [0.5, 1]}))

fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = 450,
    title = {"text": "Accounts<br><span style='font-size:0.8em;color:gray'>Subtitle</span><br><span style='font-size:0.8em;color:gray'>Subsubtitle</span>"},
    delta = {'reference': 400, 'relative': True},
    domain = {'x': [0.6, 1], 'y': [0, 1]}))

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children="Alissa's 36 years in data", style={'textAlign':'center'}),
    dcc.Graph(figure=fig)
    
])

if __name__ == '__main__':
    app.run(debug=True)

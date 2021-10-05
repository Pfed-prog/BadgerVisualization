import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go

import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)
server = app.server

app_colors = {
    'background': '#0C0F0A'
}

data=pd.read_csv('dataframe.csv')
l = data['address_multiplier'].value_counts()[:-4].index.tolist()
# Set up the app layout
app.layout = html.Div(children=[
   html.Div([html.H1(children='Dashboard: Multiplayer Address History', style={'color':"#CECECE"}),
    html.H4(children='Choose the Address to Explore', style={'color':"#CECECE"}),
    dcc.Dropdown(id='geo-dropdown',
                 options=[{'label': i, 'value': i}
                          for i in l],
                 value='0x6dEf55d2e18486B9dDfaA075bc4e4EE0B28c1545'),
    dcc.Graph(id='price-graph')]),
    html.Div([
    dcc.Dropdown(id='geo-dropdown2',
                 options=[{'label': i, 'value': i}
                          for i in l],
                 value='0x6dEf55d2e18486B9dDfaA075bc4e4EE0B28c1545'),
    dcc.Graph(id='price-graph2')]),
], style={'backgroundColor': app_colors['background'], 'margin-top':'30px'},)


# Set up the callback function
@app.callback(
    Output(component_id='price-graph', component_property='figure'),
    Input(component_id='geo-dropdown', component_property='value')
)
def update_graph(selected):
    filtered = data[data['address_multiplier'] == selected]
    line_fig = px.line(filtered,
                       x='date', y='min',
                       title=f'min: {selected}', template='plotly_dark')
    return line_fig

@app.callback(
    Output(component_id='price-graph2', component_property='figure'),
    Input(component_id='geo-dropdown2', component_property='value')
)
def update_graph(selected):
    filtered = data[data['address_multiplier'] == selected]
    line_fig = px.line(filtered,
                       x='date', y='max',
                       title=f'max:{selected}', color='address_multiplier', template='plotly_dark')
    return line_fig

# Run local server
if __name__ == '__main__':
    app.run_server(debug=True)
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

app = dash.Dash()
server = app.server

data=pd.read_csv('dataframe.csv')

# Set up the app layout
app.layout = html.Div(children=[
   html.Div([html.H1(children='Dashboard: Multiplayer Adsress History'),
    dcc.Dropdown(id='geo-dropdown',
                 options=[{'label': i, 'value': i}
                          for i in data['address_multiplier'].unique()],
                 value='0x6dEf55d2e18486B9dDfaA075bc4e4EE0B28c1545'),
    dcc.Graph(id='price-graph')]),
    html.Div([
    dcc.Dropdown(id='geo-dropdown2',
                 options=[{'label': i, 'value': i}
                          for i in data['address_multiplier'].unique()],
                 value='0x6dEf55d2e18486B9dDfaA075bc4e4EE0B28c1545'),
    dcc.Graph(id='price-graph2')]),
])


# Set up the callback function
@app.callback(
    Output(component_id='price-graph', component_property='figure'),
    Input(component_id='geo-dropdown', component_property='value')
)
def update_graph(selected):
    filtered_avocado = data[data['address_multiplier'] == selected]
    line_fig = px.line(filtered_avocado,
                       x='date', y='min',
                       title=f'min: {selected}')
    return line_fig

@app.callback(
    Output(component_id='price-graph2', component_property='figure'),
    Input(component_id='geo-dropdown2', component_property='value')
)
def update_graph(selected):
    filtered_avocado = data[data['address_multiplier'] == selected]
    line_fig = px.line(filtered_avocado,
                       x='date', y='max',
                       title=f'max:{selected}')
    return line_fig

# Run local server
if __name__ == '__main__':
    app.run_server(debug=True)
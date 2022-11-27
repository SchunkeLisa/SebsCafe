import dash
import plotly.express as px
from dash import dcc
from dash import html as html
from dash.dependencies import Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H3(children="Sebs' Cafe"),
    html.H4(children="Syrvey Data:"),
    html.Div([
        # adding bar chart
        dcc.Graph(id='bar-graph')
    ])
])


@app.callback(Output('bar-graph', 'figure'))
def plot_survey_data(base64_content, filename):
    if base64_content is None:
        return "<empty>"

    #create bar chard with xaxis femal, male and yaxis happiness
    bar_data = [["gender", "rating"]]
    with open('data01/survey.csv') as g:
        survey = g.read()
        for line in survey.splitlines():
            line = line.split(",")
            bar_data.append([line[0], line[1]])

    survey_data_figure = px.bar(bar_data, x=0, y=1, color=2, title="Profit for bought houses")

    return survey_data_figure

if __name__ == '__main__':
    app.run_server(debug=True)
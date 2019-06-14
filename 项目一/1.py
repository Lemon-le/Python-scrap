import plotly
import plotly.plotly as py
import plotly.graph_objs as go

trace = go.Table(
    header=dict(values=['A Scores', 'B Scores']),
    cells=dict(values=[[100, 90, 80, 90],
                       [95, 85, 75, 95]]))
plotly.tools.set_credentials_file(username='Lemon-le', api_key='VU1HAmJUs9iUwDf6hRP2')

data = [trace]
py.plot(data, filename = 'basic_table')

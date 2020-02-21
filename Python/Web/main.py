import dash, base64, io, pandas as pd, dash_table
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Upload(
        id='upload-image',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        multiple=True
    ),
    html.Label('Вид графика'),
    dcc.RadioItems(
        id="graph-type",
        options=[
            {'label': 'Линейный', 'value': 'scatter'},
            {'label': 'Бары', 'value': 'bar'}
        ],
        value='scatter'
    ),
    html.Div(id='output-image-upload')
])
def parse_contents(contents, filename, date, value):
    content_string = contents.split(',')[-1]
    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])
    _data_ = []
    cols = df.columns
    _x_ = [i for i in df[cols[0]]]
    for i in range(1,len(cols)):
        __d = []
        for j in df[cols[i]]:
            __d.append(j)
        _data_.append({'x':_x_,'y':__d,'type':value,'name':cols[i]})
    return html.Div([
        dcc.Graph(
        id='example-graph',
        figure={
            'data': _data_,
            'layout': {
                'title': filename
            }
        }),
        html.Hr(),
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns]
        )
    ])
@app.callback(Output('output-image-upload', 'children'),
              [Input('upload-image', 'contents'),
              Input('graph-type', 'value')],
              [State('upload-image', 'filename'),
               State('upload-image', 'last_modified')])
def update_output(list_of_contents, value, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d, value) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children
if __name__ == '__main__':
    app.run_server(debug=True)
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Dash Tutorials'),
    dcc.Graph(id='example',
              figure={
                  'data': [
                      {'x': [1, 2, 3, 4, 5], 'y': [5, 6, 7, 8, 9],
                          'type': 'line', 'name': 'boats'},
                      {'x': [1, 2, 3, 8, 5], 'y': [3, 6, 5, 2, 9],
                          'type': 'bar', 'name': 'cars'},
                  ],
                  'layout': {
                      'title': 'Basic Dash Example'
                  }
              })
])

if __name__ == '__main__':
    app.run_server(debug=True)

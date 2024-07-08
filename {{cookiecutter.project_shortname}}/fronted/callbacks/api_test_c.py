from dash.dependencies import Input, Output

from server import app
from api.system import test_api


@app.callback(
    Output('index-api-test-content-container', 'children'),
    Input('index-api-test-button', 'nClicks'),
    prevent_initial_call=True
)
def api_test(nClicks):
    
    response = test_api(
        {
            'name': 'John Doe',
            'email': 'example@163.com'
        }
    )

    return str(response)
from dash import html
from dash.dependencies import Input, Output, State
import feffery_utils_components as fuc

from server import app
from store import render_store_container
from config.env import AppConfig
from config.global_config import RouterConfig

from views import index, page_404


app.layout = html.Div(
    [
        # url监听
        fuc.FefferyLocation(id='url-container'),

        # 页面内容挂载点
        html.Div(id='app-mount'),

        # 重定向容器
        html.Div(id='redirect-container'),

        # store存储
        render_store_container(),
    ]
)


@app.callback(
    output=dict(
        app_mount=Output('app-mount', 'children'),
        redirect_container=Output('redirect-container', 'children', allow_duplicate=True),
    ),
    inputs=dict(
        pathname=Input('url-container', 'pathname')
    ),
    state=dict(
        url_trigger=State('url-container', 'trigger'),
    ),
    prevent_initial_call=True,
)
def router(pathname, url_trigger):
    if pathname in RouterConfig.BASIC_VALID_PATHNAME:
        if pathname == '/' or pathname == '/index':
            return dict(
                app_mount=index.render_content(),
                redirect_container=None
            )
        elif pathname == '/api-test':
            return dict(
                app_mount=api_test.render_content(),
                redirect_container=None
            )
        
    else:
        return dict(
            app_mount=page_404.render_content(),
            redirect_container=None
        )

        

if __name__ == '__main__':
    app.run(host=AppConfig.app_host, port=AppConfig.app_port, debug=AppConfig.app_debug)

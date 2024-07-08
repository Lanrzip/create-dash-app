from dash import html
import feffery_antd_components as fac

import callbacks.api_test_c


def render_content():

    return html.Div(
        [
            fac.AntdImage(
                src='/assets/images/plotly_logo_dark.png',
                height=200,
                preview=False
            ),
            html.H1("{{ cookiecutter.project_name }}", style={'color': '#FFFFFF'}),
            html.Div("{{ cookiecutter.description }}", style={'color': '#FFFFFF'}),
            html.Div("编辑 frontend/views/index.py 并保存以重新加载", style={'color': '#FFFFFF', 'fontSize': '36px'}),
            fac.AntdButton(
                '接口测试',
                id='index-api-test-button',
                type='primary',
                # href='/api-test',
                style={'marginTop': '20px'}
            ),
            html.Div(
                id='index-api-test-content-container',
                style={
                    'marginTop': '20px',
                    'height': '200px',
                    'width': '400px',
                    'backgroundColor': '#FFFFFF',
                    'borderRadius': '6px',
                    'border': '1px solid #D9D9D9',
                }
            )
        ],
        style={
            'height': '100vh',
            'width': '100vw',
            'display': 'flex',
            'alignItems': 'center',
            'justifyContent': 'center',
            'flexDirection': 'column',
            'backgroundColor': '#0E1012'
        }
    )
import os
import time
import dash
from loguru import logger
from config.env import AppConfig
from config.global_config import PathConfig


app = dash.Dash(
    __name__,
    compress=True,
    suppress_callback_exceptions=True,
    update_title=None,
    external_scripts=[

    ]
)

server = app.server

app.server.secret_key = AppConfig.app_secret_key

log_time = time.strftime("%Y%m%d", time.localtime())
api_log_file_path = os.path.join(PathConfig.ABS_ROOT_PATH, 'log', 'api_log', f'api_request_log_{log_time}.log')
logger.add(api_log_file_path, filter=lambda x: '[api]' in x['message'],
           rotation="50MB", encoding="utf-8", enqueue=True, compression="zip")
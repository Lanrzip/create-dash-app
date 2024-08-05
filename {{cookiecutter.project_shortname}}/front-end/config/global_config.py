import os
from config.env import AppConfig


class PathConfig:

    # 项目绝对根目录
    ABS_ROOT_PATH = os.path.abspath(os.getcwd())


class RouterConfig:

    # 合法pathname列表
    BASIC_VALID_PATHNAME = [
        '/', '/index', '/api-test'
    ]

    # 静态路由列表
    STATIC_VALID_PATHNAME = ['/', '/index', '/api-test']


class ApiBaseUrlConfig:

    BaseUrl = AppConfig.app_base_url + AppConfig.app_proxy_path if AppConfig.app_is_proxy else AppConfig.app_base_url


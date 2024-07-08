from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):

    app_env: str = 'dev'
    app_name: str = "{{cookiecutter.project_name}}"
    app_base_url: str = 'http://127.0.0.1:9099'  # fastapi服务地址
    app_proxy_path: str = '/dev-api'
    app_is_proxy: bool = False
    app_secret_key: str = "{{ cookiecutter.project_name.upper()|replace(' ', '-')|replace('_', '-') }}"
    app_host: str = 'localhost'
    app_port: int = 8088
    app_debug: bool = True
    # app_compress_algorithm: str = 'br'
    # app_compress_br_level: int = 11


AppConfig = AppSettings()
from utils.request import api_request


def test_api(params: dict):

    return api_request(method='post', url='/system/api-test', is_headers=False, json=params)
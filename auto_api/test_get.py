import requests
import json

URL = 'https://api.github.com'


def build_uri(endpoint):
    return '/'.join([URL, endpoint])  # 主要作用是拼接接口请求地址


def better_output(json_str):
    return json.dumps(json.loads(json_str), indent=4)  # json格式化输出


def request_method():
    response = requests.get(build_uri('users/haropy'))  # 调用get方法
    print(better_output(response.text))  # 调用json格式化输出


def params_method():
    response = requests.get(build_uri('users'), params={'since': 11})
    print(better_output(response.text))
    print(response.headers)
    print(response.url)


if __name__ == '__main__':
    request_method()

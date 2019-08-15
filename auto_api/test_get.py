import json

import requests

URL = 'https://api.github.com'


def build_uri(endpoint):
    return '/'.join([URL, endpoint])  # 主要作用是拼接接口请求地址


def better_output(json_str):
    return json.dumps(json.loads(json_str), indent=4)  # 采用json里面提供方法打印出来，格式更好看


def request_method():
    response = requests.get(build_uri('users/Anthonyliu86'))  # 调用get方法，注意用户名这个地方写法，没有图片中冒号
    print(better_output(response.text))  # 调用json更好格式输出


def params_method():
    response = requests.get(build_uri('users'), params={'since': 11})
    print(better_output(response.text))
    print(response.headers)
    print(response.url)


def json_method():
    response = requests.patch(build_uri('user'), auth=('your_account', 'your_password'), json={'email':
                                                                                                   'abc@msn.com',
                                                                                               'name': 'Anthony_tester'})
    print(better_output(response.text))
    print(response.headers)
    print(response.url)


if __name__ == '__main__':
    json_method()

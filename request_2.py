import requests
from concurrent.futures import ThreadPoolExecutor

URLS = [
    'http://echo.jsontest.com/key/value/test/1',
    'http://echo.jsontest.com/key/value/test/2',
    'http://echo.jsontest.com/key/value/test/3',
    'http://echo.jsontest.com/key/value/test/4',
    'http://echo.jsontest.com/key/value/test/5',
    'http://echo.jsontest.com/key/value/test/6',
]


def call(url):
    resp = requests.get(url)
    print(resp.status_code)
    print(resp.json())

if __name__ == '__main__':
    # [call(url) for url in URLS]

    executor = ThreadPoolExecutor(max_workers=10)
    executor.map(call, URLS)

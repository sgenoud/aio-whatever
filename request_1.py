import requests

URL = 'http://echo.jsontest.com/key/value/one/two'

def call(url):
    resp = requests.get(url)
    print(resp.status_code)
    print(resp.json())

if __name__ == '__main__':
    call(URL)

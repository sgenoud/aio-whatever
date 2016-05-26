
import aiohttp
import asyncio

URLS = [
    'http://echo.jsontest.com/key/value/test/1',
    'http://echo.jsontest.com/key/value/test/2',
    'http://echo.jsontest.com/key/value/test/3',
    'http://echo.jsontest.com/key/value/test/4',
    'http://echo.jsontest.com/key/value/test/5',
    'http://echo.jsontest.com/key/value/test/6',
]

async def call(url):
    async with aiohttp.get(url) as resp:
        print(resp.status)
        print(await resp.json())

if __name__ == '__main__':
    calls = asyncio.wait([call(url) for url in URLS])
    asyncio.get_event_loop().run_until_complete(calls)

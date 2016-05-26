import asyncio
import aiohttp

URL = 'http://echo.jsontest.com/key/value/one/two'

async def call(url):
    async with aiohttp.get(url) as resp:
        print(resp.status)
        print(await resp.json())


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(call(URL))

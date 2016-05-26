from aiohttp import web
import asyncio
app = web.Application()

async def hello(request):
    name = request.match_info.get('name', "Anonymous")
    await asyncio.sleep(2)
    return web.json_response({
        'hello': name,
    })

app.router.add_route('GET', '/hello/{name}', hello)

web.run_app(app)

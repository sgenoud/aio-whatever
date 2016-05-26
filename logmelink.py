from aiohttp import web
import asyncio

async def fetch_info(request):
    secret = request.match_info.get('secret')
    redis_pool = request.app['redis_pool']
    redis_sub_pool = request.app['redis_subscribe_pool']

    # ... deal with some default cases

    async with redis_sub_pool.get() as redis_sub:
        channel, = await redis_sub.subscribe(secret)

        done, not_done = await asyncio.wait([channel.get(encoding='utf-8')], timeout=30)
        await redis_sub.unsubscribe(secret)

    async with redis_pool.get() as redis:
        info = await _info(redis, secret)

    return web.json_response(info)

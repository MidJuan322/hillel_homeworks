import asyncio
import aiohttp
import json
from pprint import pprint


async def request_data(url):
    async with aiohttp.request('GET', url) as data:
        return await data.text()


async def get_reddit_top(subreddit):
    data = json.loads(await request_data(f'https://www.reddit.com/r/{subreddit}/top.json?sort=top&t=day&limit=5'))
    rez_dict = {subreddit: {}}
    for post in data['data']['children']:

        temp_dict = {post['data']['title']: {
            'score': post['data']['score'],
            'link': f"https://www.reddit.com{post['data']['permalink']}"
        }}

        rez_dict[subreddit].update(temp_dict)
    return rez_dict


async def main():
    reddits = {"python", "compsci", "microbork"}
    res = await asyncio.gather(*(get_reddit_top(u) for u in reddits))
    rez_dict = {}

    for i in res:
        for key, value in i.items():
            rez_dict[key] = value

    return rez_dict


loop = asyncio.get_event_loop()
pprint(loop.run_until_complete(main()))
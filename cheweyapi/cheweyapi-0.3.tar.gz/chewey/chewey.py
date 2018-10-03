import asyncio
import aiohttp
import json


class Client:
	def __init__(self, token):
		self.token = token

	async def dog(self):
		async with aiohttp.ClientSession() as cs:
			async with cs.get(f'http://api.chewey-bot.ga/dog/?auth={self.token}') as r:
				r = await r.json()
		return r['data']

	async def cat(self):
		async with aiohttp.ClientSession() as cs:
			async with cs.get(f'http://api.chewey-bot.ga/cat/?auth={self.token}') as r:
				r = await r.json()
		return r['data']

	async def birb(self):
		async with aiohttp.ClientSession() as cs:
			async with cs.get(f'http://api.chewey-bot.ga/birb/?auth={self.token}') as r:
				r = await r.json()
		return r['data']

	async def fantasy_art(self):
		async with aiohttp.ClientSession() as cs:
			async with cs.get(f'http://api.chewey-bot.ga/fantasy-art/?auth={self.token}') as r:
				r = await r.json()
		return r['data']

	async def space(self):
		async with aiohttp.ClientSession() as cs:
			async with cs.get(f'http://api.chewey-bot.ga/space/?auth={self.token}') as r:
				r = await r.json()
		return r['data']

	async def plane(self):
		async with aiohttp.ClientSession() as cs:
			async with cs.get(f'http://api.chewey-bot.ga/plane/?auth={self.token}') as r:
				r = await r.json()
		return r['data']

	async def otter(self):
		async with aiohttp.ClientSession() as cs:
			async with cs.get(f'http://api.chewey-bot.ga/otter/?auth={self.token}') as r:
				r = await r.json()
		return r['data']

	async def rabbit(self):
		async with aiohttp.ClientSession() as cs:
			async with cs.get(f'http://api.chewey-bot.ga/rabbit/?auth={self.token}') as r:
				r = await r.json()
		return r['data']

	async def snake(self):
		async with aiohttp.ClientSession() as cs:
			async with cs.get(f'http://api.chewey-bot.ga/snake/?auth={self.token}') as r:
				r = await r.json()
		return r['data']

	async def car(self):
		async with aiohttp.ClientSession() as cs:
			async with cs.get(f'http://api.chewey-bot.ga/car/?auth={self.token}') as r:
				r = await r.json()
		return r['data']
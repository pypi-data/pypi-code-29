import logging
import random
import aiohttp
from urllib import parse
import discord
from discord.ext.commands import Bot

# TODO Stocks, ?dow ?nyse cvs
# TODO ?stats - # messages, number of new joins over time (Generate image and upload?)
# TODO add "Roll" for dice roll
# TODO Weather?
# TODO Define?
# TODO urbandefine?
# TODO fortune cookie
# TODO !remind me
# TODO On ready announce to server or to channel - I'm here to help! Just type ?help in the #help-desk channel.
# TODO Joke command
# TODO color commands? like pbot
# TODO crypto commands like pbot?
# TODO news or feed command


BOT_PREFIX = ("?", "!")


class HelpDeskBot:

    def __init__(self, channel_name, token_file_name, debug_file_name):
        logging.basicConfig(
            filename=debug_file_name,
            level=logging.INFO,
            format='%(asctime)s %(module)s %(msg)s',
        )
        logging.info("[*] Initializing bot...")
        with open(token_file_name) as token_file:
            self.token = token_file.read().strip()
        self.designated_channel_name = channel_name
        self.client = Bot(command_prefix=BOT_PREFIX)
        self.setup()

    def run(self):
        logging.info("[*] Running...")
        self.client.run(self.token)

    def setup(self):

        @self.client.event
        async def on_ready():
            logging.info("[+] Connected as " + self.client.user.name)
            logging.info("[+] Listening for private messages and in channel #" + self.designated_channel_name)
            await self.client.change_presence(game=discord.Game(name='Help Desk'))

        @self.client.event
        async def on_message(message):
            # Ignore messages by bots (including self)
            if message.author.bot:
                return

            # Only return help in designated channel
            if message.content.startswith(BOT_PREFIX):
                msg = message.content.strip("".join(list(BOT_PREFIX)))
                if msg.startswith("help"):
                    if not message.channel.is_private and message.channel.name != self.designated_channel_name:
                        return

            # Pass on to rest of the client commands
            if message.content.startswith(BOT_PREFIX):
                await self.client.process_commands(message)

        @self.client.command(description="Checks the current Bitcoin price in US Dollars from Coinbase.",
                             brief="Get current Bitcoin price",
                             aliases=['btc'],
                             pass_context=True)
        async def bitcoin(context):
            # Only respond to the channel designated and private messages.
            if not context.message.channel.is_private and context.message.channel.name != self.designated_channel_name:
                return

            url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
            async with aiohttp.ClientSession() as session:
                raw_response = await session.get(url)
                response = await raw_response.json(content_type='application/javascript')
                await self.client.say("Bitcoin price is: $" + response['bpi']['USD']['rate'])

        @self.client.command(name='8ball',
                             description="Answers a yes/no question.",
                             brief="Answers from the beyond.",
                             aliases=['eight_ball', 'eightball', '8-ball'],
                             pass_context=True)
        async def eight_ball(context):
            # Only respond to the channel designated and private messages.
            if not context.message.channel.is_private and context.message.channel.name != self.designated_channel_name:
                return
            possible_responses = [
                'That is a resounding no',
                'It is not looking likely',
                'Too hard to tell',
                'It is quite possible',
                'Definitely',
            ]
            await self.client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

        @self.client.command(name='lmgtfy',
                             description="Let me Google that for you",
                             brief="Google help",
                             aliases=['letmegooglethatforyou', 'trygoogle', 'googlefirst'],
                             pass_context=True)
        async def lmgtfy(context):
            search_term = context.message.content.strip("".join(list(BOT_PREFIX))).replace("lmgtfy", "").strip()
            if search_term == "":
                return
            url = 'https://lmgtfy.com?' + parse.urlencode({"q": search_term})
            response = "Here is the link you requested: " + url
            await self.client.say(response)

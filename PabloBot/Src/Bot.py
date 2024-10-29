import os
import discord

from dotenv import load_dotenv
from discord.ext import commands
from groq import Groq

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))
API_KEY = os.getenv('API_KEY')

ai = Groq(api_key=API_KEY)
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

chat_completion = ai.chat.completions.create(
    messages=[
        {
        "role": "user",
        "content": ("Make a complement for Pablo the Husky by taking a random prompt from the list below"
                    "and making a variation while keeping it informal. "
                    "do not preface your response and only provide the single complement itself without quotes"
                    "List is provided below"
                    "Whos a good boyyy? Pablooo is!"
                    "Pablo! The bestest boyyy!"
                    "Ohhhh, look at this lil' cutie, Pablo!"
                    "Who's the fluffiest floof? Thats right, its Pablo!"
                    "Pablo, you handsome lil' pupper!"
                    "Somebody give Pablo all the treats!"
                    "Pablo, king of belly rubs!"
                    "Smooches for Pablo, the sweetest pup!"
                    "Who's got the cutest paws? Pablo does!"
                    "Pablo, the tail-wagging champion!"
                    ),
        }
    ],
    model="llama3-8b-8192",
    temperature=0.2,
    top_p=0.9,
   
)

@bot.event
async def on_message(message):
    if message.channel.id != CHANNEL_ID or message.author.bot:
        return
    await bot.process_commands(message)

    if message.attachments:
        for attachment in message.attachments:
            if attachment.content_type.startswith("image/"):
                await message.channel.send(chat_completion.choices[0].message.content)
            return

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

bot.run(TOKEN)
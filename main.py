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

def generate_response():
    chat_completion = ai.chat.completions.create(
        messages=[
            {
            "role": "user",
            "content": ("Make a compliment for Pablo the Husky by choosing a random prompt"
                        "and making a variation of the corresponding compliment below\n "
                        "do not preface your response and only provide the single short compliment itself without quotes\n"
                        "Whos a good boyyy? Pablooo is!\n"
                        "Pablo! The bestest boyyy!\n"
                        "Ohhhh, look at this lil' cutie, Pablo!\n"
                        "Who's the fluffiest floof? Thats right, its Pablo!\n"
                        "Pablo, you handsome lil' pupper!\n"
                        "Somebody give Pablo all the treats!\nn"
                        "Pablo, king of belly rubs!\n"
                        "Smooches for Pablo, the sweetest pup!\n"
                        "Who's got the cutest paws? Pablo does!\n"
                        " Pablo, the tail-wagging champion!\n"
                        " Pablo, did you know youre the best boy ever?\n"
                        " If cuteness was a contest, Pablo would win every day!\n"
                        " Ohhh, Pablo, youre just too adorable!\n"
                        " Whos the snuggliest? It's Pablo!\n"
                        " Pablos giving everyone puppy eyes... he knows hes cute!\n"
                        " Who's a total heart-stealer? Pablo!\n"
                        " Big stretch! Big yawn! Good boy, Pablo!\n"
                        " Pablo alert! Cuteness overload!\n"
                        " Can we all just agree that Pablo is THE good boy?\n"
                        " Pablo, you make the world a better place!\n"
                        " Who's got the best puppy smile? Pablooo!\n"
                        " Pablo, Id follow you to the ends of the yard!\n"
                        " Pablo, what a lovable fluff ball!\n"
                        ),
            }
        ],
        model="llama-3.3-70b-versatile",
        temperature=2,
        top_p=1,
        
    )
    return chat_completion.choices[0].message.content

@bot.event
async def on_message(message):
    if message.channel.id != CHANNEL_ID or message.author.bot:
        return
    await bot.process_commands(message)

    if message.attachments:
        for attachment in message.attachments:
            if attachment.content_type.startswith("image/"):
                
                await message.channel.send(generate_response())
            return

bot.run(TOKEN)
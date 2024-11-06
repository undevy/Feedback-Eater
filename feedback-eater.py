import discord
from pymongo import MongoClient

TOKEN = os.getenv('DISCORD_BOT_TOKEN')

MONGODB_URI = os.getenv('MONGODB_URI')

CHANNEL_ID = '1178694908064841728'

client = discord.Client()
mongo_client = MongoClient(MONGODB_URI)
db = mongo_client['discord_data']
collection = db['messages']

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.channel.id == CHANNEL_ID:
        await collection.insert_one({
            'author': str(message.author),
            'content': message.content,
            'timestamp': message.created_at
        })
        print(f"Saved message from {message.author}: {message.content}")

client.run(TOKEN)

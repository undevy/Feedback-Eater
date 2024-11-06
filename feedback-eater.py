{\rtf1\ansi\ansicpg1252\cocoartf2820
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww18120\viewh10620\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import discord\
from pymongo import MongoClient\
\
TOKEN = 'MTMwMzczMDk3MDk2NDM5Mzk5NA.GElmdx.tts1qZR_iqylnoEXGEkWz4JfxvHtIaCAUWn6Ck'\
\
# \uc0\u1047 \u1072 \u1084 \u1077 \u1085 \u1080 \u1090 \u1077  \u1085 \u1072  \u1089 \u1090 \u1088 \u1086 \u1082 \u1091  \u1087 \u1086 \u1076 \u1082 \u1083 \u1102 \u1095 \u1077 \u1085 \u1080 \u1103  \u1082  MongoDB\
MONGODB_URI = 'mongodb+srv://kier:UgW86VVyHRHfAyD@feedback-eater.i0udy.mongodb.net/?retryWrites=true&w=majority&appName=feedback-eater'\
\
CHANNEL_ID = '1178694908064841728'\
\
client = discord.Client()\
mongo_client = MongoClient(MONGODB_URI)\
db = mongo_client['discord_data']\
collection = db['messages']\
\
@client.event\
async def on_ready():\
    print(f'\{client.user.name\} has connected to Discord!')\
\
@client.event\
async def on_message(message):\
    if message.channel.id == CHANNEL_ID:\
        await collection.insert_one(\{\
            'author': str(message.author),\
            'content': message.content,\
            'timestamp': message.created_at\
        \})\
        print(f"Saved message from \{message.author\}: \{message.content\}")\
\
client.run(TOKEN)}
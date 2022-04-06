#https://discordapp.com/oauth2/authorize?client_id=736671500517507094&scope=bot&permissions=100352
import aiohttp
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option, create_choice
from discord import Game, Client
from tinydb import TinyDB, Query
from tinydb.operations import delete
from timeit import timeit
from secret import token2, token3

client = Client()
slash = SlashCommand(client, sync_commands=True)
guild_ids = [456263185692098561]

@slash.slash(name="willow",description="Sends a list for overwillow", guild_ids=guild_ids)
async def _willow(ctx):
    await ctx.defer()
    db = TinyDB('db.json')
    Hammer = Query()
    auth = {"Authorization":"Bearer {}".format(token3)}
    async with aiohttp.ClientSession() as session:
        db.truncate()
        async with session.get('https://api.clashroyale.com/v1/clans/%2399LRYVQQ/members', headers = auth) as a:
            if a.status == 200:
                a = await a.json()
                db.insert_multiple(a["items"])
        async with session.get('https://api.clashroyale.com/v1/clans/%2399LRYVQQ/currentriverrace', headers=auth) as b:
            if b.status == 200:
                b = await b.json()
                b = b['clan']['participants']
                for i in b:
                    db.update(i, Hammer.tag == i['tag'])
    db.remove((Hammer.role == 'leader') | (Hammer.role == 'coLeader'))

    c = db.search((Hammer.role == 'member') & (Hammer.donations > 250) & (Hammer.decksUsed >= 12))
    kickstring = "__Promotions({})__\n".format(len(c))
    for i in c:
        kickstring += "[" + i["name"] + "]"

    c = db.search((Hammer.role == 'elder') & ((Hammer.donations < 200) | (Hammer.decksUsed < 12)))
    kickstring += "\n\n__Demotions({})__\n".format(len(c))
    for i in c:
        kickstring += "[" + i["name"] + "]"

    kickstring += "\n\n__Kicks__"

    c = db.search((Hammer.role == 'member') & (Hammer.donations == 0) & (Hammer.decksUsed == 0))
    if(len(c) > 0):
        kickstring += "\n**No war & no donations: **"
        for i in c:
            kickstring += "[" + i["name"] + "]"
    db.remove((Hammer.role == 'member') & (Hammer.donations == 0) & (Hammer.decksUsed == 0))

    c = db.search((Hammer.role == 'member') & (Hammer.donations < 100) & (Hammer.decksUsed == 0))
    if(len(c) > 0):
        kickstring += "\n**No war & low donations: **"
        for i in c:
            kickstring += "[" + i["name"] + "]"
    db.remove((Hammer.role == 'member') & (Hammer.donations < 100) & (Hammer.decksUsed == 0))

    c = db.search((Hammer.role == 'member') & (Hammer.donations == 0) & (Hammer.decksUsed < 8))
    if(len(c) > 0):
        kickstring += "\n**Low war & no donations: **"
        for i in c:
            kickstring += "[" + i["name"] + "]"
    db.remove((Hammer.role == 'member') & (Hammer.donations == 0) & (Hammer.decksUsed < 8))

    c = db.search((Hammer.role == 'member') & (Hammer.decksUsed == 0))
    if(len(c) > 0):
        kickstring += "\n**No war: **"
        for i in c:
            kickstring += "[" + i["name"] + "]"
    db.remove((Hammer.role == 'member') & (Hammer.decksUsed == 0))

    c = db.search((Hammer.role == 'member') & (Hammer.donations == 0))
    if(len(c) > 0):
        kickstring += "\n**No donations: **"
        for i in c:
            kickstring += "[" + i["name"] + "]"
    db.remove((Hammer.role == 'member') & (Hammer.donations == 0))

    c = db.search((Hammer.role == 'member') & (Hammer.donations < 100) & (Hammer.decksUsed < 8))
    if(len(c) > 0):
        kickstring += "\n**Low war & low donations: **"
        for i in c:
            kickstring += "[" + i["name"] + "]"
    db.remove((Hammer.role == 'member') & (Hammer.donations < 100) & (Hammer.decksUsed < 8))

    c = db.search((Hammer.role == 'member') & (Hammer.decksUsed < 8))
    if(len(c) > 0):
        kickstring += "\n**Low war: **"
        for i in c:
            kickstring += "[" + i["name"] + "]"
    db.remove((Hammer.role == 'member') & (Hammer.decksUsed < 8))

    c = db.search((Hammer.role == 'member') & (Hammer.donations < 100))
    if(len(c) > 0):
        kickstring += "\n**Low donations: **"
        for i in c:
            kickstring += "[" + i["name"] + "]"
    db.remove((Hammer.role == 'member') & (Hammer.donations < 100))

    await ctx.send(kickstring)


@slash.slash(name="kindom", description="Sends a kicklist for bkindom", guild_ids=guild_ids)
async def _kindom(ctx):
    db = TinyDB('db.json')
    Hammer = Query()
    auth = {"Authorization":"Bearer {}".format(token3)}
    async with aiohttp.ClientSession() as session:
        db.truncate()
        async with session.get('https://api.clashroyale.com/v1/clans/%23JGLJR8L/members', headers = auth) as a:
            if a.status == 200:
                a = await a.json()
                db.insert_multiple(a["items"])
        async with session.get('https://api.clashroyale.com/v1/clans/%23JGLJR8L/currentriverrace', headers=auth) as b:
            if b.status == 200:
                b = await b.json()
                b = b['clan']['participants']
                for i in b:
                    db.update(i, Hammer.tag == i['tag'])
    db.remove((Hammer.role == 'leader') | (Hammer.role == 'coLeader') | (Hammer.role == 'elder'))

    kickstring = ""
    c = db.search((Hammer.donations == 0) & (Hammer.decksUsed == 0))
    if(len(c) > 0):
        kickstring += "\n\n__No war & no donations__\n"
        for i in c:
            kickstring += "[" + i["name"] + "]"
    db.remove((Hammer.donations == 0) & (Hammer.decksUsed == 0))

    c = db.search(Hammer.decksUsed == 0)
    if(len(c) > 0):
        kickstring += "\n\n__No war__\n"
        for i in c:
            kickstring += "[" + i["name"] + "]"
    db.remove(Hammer.decksUsed == 0)

    c = db.search(Hammer.donations == 0)
    if(len(c) > 0):
        kickstring += "\n\n__No donations__\n"
        for i in c:
            kickstring += "[" + i["name"] + "]"
    db.remove(Hammer.donations == 0)
    await ctx.send(kickstring)

@slash.slash(name="morrow", description="Shows current deadness of overmorrow", guild_ids=guild_ids)
async def _morrow(ctx):
    db = TinyDB('db.json')
    Hammer = Query()
    auth = {"Authorization":"Bearer {}".format(token3)}
    async with aiohttp.ClientSession() as session:
        db.truncate()
        async with session.get('https://api.clashroyale.com/v1/clans/%2399U9QJRR/members', headers = auth) as a:
            if a.status == 200:
                a = await a.json()
                db.insert_multiple(a["items"])
        async with session.get('https://api.clashroyale.com/v1/clans/%2399U9QJRR/currentriverrace', headers=auth) as b:
            if b.status == 200:
                b = await b.json()
                b = b['clan']['participants']
                for i in b:
                    db.update(i, Hammer.tag == i['tag'])
    db.remove((Hammer.role == 'leader') | (Hammer.role == 'coLeader'))

    c = db.search((Hammer.donations == 0) & (Hammer.decksUsed == 0))
    await ctx.send("Number of people with 0 0: " + str(len(c)))

client.run(token2, reconnect=True)

#Whenever I set a variable to "redacted", replace it with sth of your own
import aiohttp
from discord_slash import SlashCommand
from discord import Client
from subprocess import check_output
from secret import token1

owner_id="redacted"
client = Client(owner_id=owner_id)
slash = SlashCommand(client, sync_commands=True)
guild_ids = ["redacted","redacted"]

async def apifetch(ctx,url,key):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            if r.status == 200:
                js = await r.json()
                await ctx.send(js[key])
            else:
                await ctx.send("api down")

@slash.slash(name="fox", description="Sends a picture of a fox", guild_ids=guild_ids)
async def _fox(ctx):
    await apifetch(ctx, 'https://randomfox.ca/floof/', 'image')

@slash.slash(name="dog", description="Sends a picture of a dog", guild_ids=guild_ids)
async def _dog(ctx):
    await apifetch(ctx, 'https://dog.ceo/api/breeds/image/random', 'message')

@slash.slash(name="cat", description="Sends a picture of a cat", guild_ids=guild_ids)
async def _cat(ctx):
    await apifetch(ctx, 'http://aws.random.cat/meow', 'file')

@slash.slash(name="bomb", description='"One with everything" ~Confucius', guild_ids=guild_ids)
async def _bomb(ctx):
    await apifetch(ctx, 'https://randomfox.ca/floof/', 'image')
    await apifetch(ctx, 'http://aws.random.cat/meow', 'file')
    await apifetch(ctx, 'https://dog.ceo/api/breeds/image/random', 'message')

#The Clash Royale api (see kicklistbot) is IP locked, meaning I need to update the keys when my ISP changes my public IP. This method speeds up that process
@slash.slash(name="patch", description="Change Token of IP locked api when your IP changes", guild_ids=guild_ids)
async def _patch(ctx, newtoken = ""):
    if(ctx.author.id == owner_id):
        if(newtoken == ""):
            a = check_output("curl ifconfig.me", shell = True)
            await ctx.send(a.decode("utf-8"))
        else:
            with open('secret.py', 'a') as tokenbase:
                tokenbase.write("token3 = '" + newtoken + "'")
            await ctx.send("token updated")
    else:
        await ctx.send("Only Ura can use this command")

client.run(token1, bot=True, reconnect=True)

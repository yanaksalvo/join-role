import discord
from discord.ext import commands

TOKEN = ''
GUILD_ID =  
ROLE_ID = 

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} is connected to Discord!')

@bot.event
async def on_member_join(member):
    guild = bot.get_guild(GUILD_ID)
    role = guild.get_role(ROLE_ID)

    await member.add_roles(role)
    print(f'{member.name} joined and got the role {role.name}!')

bot.run(TOKEN)
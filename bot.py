import os
#deez
import discord
from dotenv import load_dotenv
from discord.ext import commands
from leaderboard import Leaderboard
from payout import Payout
from player import Player
from race import Race

load_dotenv('token.env')
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='$', intents = intents)
leaderboard = None
payout = None
race = None

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    guild = discord.utils.get(bot.guilds, name='testserver')
    members = guild.members
    players = []
    for member in members:
        if (member.display_name == bot.user.display_name):
            pass
        else:
            player = Player(member.display_name)
            players.append(player)
    bot.leaderboard = Leaderboard(players)
    for leaderboardPlayer in bot.leaderboard.players:
        print(leaderboardPlayer.name)

@bot.command(name='openbets', help='registers the calling user to the gambling game')
async def openBets(ctx):
    roles = ctx.author.roles
    flag = 0
    message = ''
    for role in roles:
        if (role.name == 'admin'):
            flag = 1
    if flag == 1:
        bot.race = Race()
        bot.payout = Payout(race)
        message = 'Bets are now open'
    else:
        message = 'You are not permitted to use this command'
    await ctx.send(message)

bot.run(TOKEN)


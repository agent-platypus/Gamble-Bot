import os
import helpers
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
discBot = commands.Bot(command_prefix='$', intents = intents)
leaderboard = None
payout = None
race = None

@discBot.event
async def on_ready():
    global leaderboard
    print(f'{discBot.user} has connected to Discord!')
    guild = discord.utils.get(discBot.guilds, name='testserver')
    members = guild.members
    players = []
    for member in members:
        if (member.display_name == discBot.user.display_name):
            pass
        else:
            player = Player(member.display_name, member.id)
            players.append(player)
    leaderboard = Leaderboard(players)
    for leaderboardPlayer in leaderboard.players:
        print(leaderboardPlayer.name)

@discBot.command(name='openbets', help='opens up a new race to bet on (admin only)')
async def openBets(ctx):
    global payout
    global race
    if (not(payout is None) or not(race is None)):
        message = 'There is already a game in place, if you would like to start a new game, please finish the existing one first'
    else:
        roles = ctx.author.roles
        flag = 0
        message = ''
        for role in roles:
            if (role.name == 'admin'):
                flag = 1
        if flag == 1:
            race = Race()
            payout = Payout(race)
            message = helpers.generateOpenBetsMessage(race)
        else:
            message = 'You are not permitted to use this command'
    await ctx.send(message)

@discBot.command(name = 'bet', help = 'add a bet by calling this command followed by the horse name you want to bet on, and the amount you want to bet')
async def bet(ctx):
    pass

@discBot.command(name = 'rank', help = 'see your rank on the leaderboard')
async def rank(ctx):
    global leaderboard
    message = ''
    for i in range (len(leaderboard.players)):
        if ctx.author.id == leaderboard.players[i].id:
            message = 'You are currently rank ' + str(i + 1) + ' with a balance of ' + str(leaderboard.players[i].money)
    await ctx.send(message)
discBot.run(TOKEN)


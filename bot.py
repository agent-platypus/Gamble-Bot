
import os
from errors import AmountTooLargeError, AmountTooSmallError, HorseMissingError, MultipleBetError
import helpers
#deez
import discord
from dotenv import load_dotenv
from discord.ext import commands
from leaderboard import Leaderboard
from payout import Payout
from player import Player
from race import Race
import pickle

load_dotenv('token.env')
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.members = True
discBot = commands.Bot(command_prefix='$', intents = intents)
leaderboard = None
payout = None
race = None
guild = None

@discBot.event
async def on_ready():
    global leaderboard
    global guild
    global payout
    global race
    guild = discord.utils.get(discBot.guilds, name='testserver')
    print(f'{discBot.user} has connected to Discord!')
    try:
        leaderboard = pickle.load(open("leaderboard.pickle", "rb"))
    except (OSError, IOError) as e:
        members = guild.members
        players = []
        for member in members:
            if (member.display_name == discBot.user.display_name):
                pass
            else:
                player = Player(member.display_name, member.id)
                players.append(player)
        leaderboard = Leaderboard(players)
        pickle.dump(leaderboard, open("leaderboard.pickle", "wb"))
    try:
        payout = pickle.load(open('payout.pickle', 'rb'))
        race = pickle.load(open('race.pickle', 'rb'))
    except:
        pass
    for leaderboardPlayer in leaderboard.players:
        print(leaderboardPlayer.name)

#@discBot.event
#async def on_member_join(member):
 #   player = Player(member.display_name, member.id)
  #  leaderboard.addPlayer(player)

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
            pickle.dump(race, open('race.pickle', 'wb'))
            pickle.dump(payout, open('payout.pickle', 'wb'))
            role = guild.get_role(975192638594625577)
            message = role.mention + ' ' + helpers.generateOpenBetsMessage(race)
        else:
            message = 'You are not permitted to use this command'
    await ctx.send(message)

@discBot.command(name = 'rank', help = 'see your rank on the leaderboard')
async def rank(ctx):
    global leaderboard
    message = ''
    for i in range (len(leaderboard.players)):
        if ctx.author.id == leaderboard.players[i].id:
            message = 'You are currently rank ' + str(i + 1) + ' with a balance of ' + str(leaderboard.players[i].money)
    await ctx.send(message)

@discBot.command(name = 'leaderboard', help = 'show leaderboard')
async def leaderboard(ctx):
    global leaderboard
    message = helpers.generateLeaderboardMessage(leaderboard)
    await ctx.send(message)

@discBot.command(name = 'bet', help = 'bet an amount on a horse, should be formatted like Ex. bet horsey 100')
async def bet(ctx):
    global payout
    global leaderboard
    if (payout is None):
        message = 'There is currently no race available to bet on, please open bets first'
    else:
        args = ctx.message.content.split()
        if len(args) != 3:
            await ctx.send('Error: invalid number of arguments')
            return
        horse = args[1]
        amount = args[2]
        playerID = ctx.author.id
        for player in leaderboard.players:
            if playerID == player.id:
                try:
                    payout.addBet(player, horse, int(amount))
                    pickle.dump(payout, open('payout.pickle', 'wb'))
                    message = 'Your bet was successfully added'
                except AmountTooSmallError:
                    message = 'Error: your bet is zero or negative'
                except AmountTooLargeError:
                    message = 'Error: your bet is too large'
                except HorseMissingError:
                    message = 'Error: this horse does not exist'
                except MultipleBetError:
                    message = 'Error: you have already placed a bet. If you would like to remove your bet, use $removebet'
                break
    await ctx.send(message)

@discBot.command(name = 'startrace', help = 'start the race (admin only)')
async def startRace(ctx):
    global payout
    global race
    global leaderboard
    if (payout is None):
        message = 'There is currently no race, please open bets first'
    else:
        roles = ctx.author.roles
        flag = 0
        message = ''
        for role in roles:
            if (role.name == 'admin'):
                flag = 1
        if flag == 1:
            winner = race.startRace()
            winners = payout.payoutPlayers(winner)
            leaderboard.sortLeaderboard()
            pickle.dump(leaderboard, open("leaderboard.pickle", "wb"))
            message = helpers.generateStartRaceMesage(winner, winners, guild)
            payout = None
            race = None
            pickle.dump(payout, open('payout.pickle', 'wb'))
            pickle.dump(race, open('race.pickle', 'wb'))
        else:
            message = 'You are not permitted to use this command'
    await ctx.send(message)

@discBot.command(name = 'allowance', help = 'give all players their allowance (admin only)')
async def allowance(ctx):
    global leaderboard
    allowance = 100
    roles = ctx.author.roles
    flag = 0
    message = ''
    for role in roles:
        if (role.name == 'admin'):
            flag = 1
    if flag == 1:
        for player in leaderboard.players:
            player.addMoney(allowance)
        message = 'Allowance of ' + str(allowance) +  ' has been given to all players'
    else:
        message = 'You are not permitted to use this command'
    await ctx.send(message)

@discBot.command(name = 'addplayer', help = 'add a player to the leaderboard (admin only)')
async def addPlayer(ctx):
    global leaderboard
    roles = ctx.author.roles
    flag = 0
    message = ''
    for role in roles:
        if (role.name == 'admin'):
            flag = 1
    if flag == 1:
        args = ctx.message.content.split()
        if len(args) != 2:
            await ctx.send('Error: invalid number of arguments')
            return
        name = args[1]
        for member in guild.members:
            if (name == member.display_name):
                player = Player(member.display_name, member.id)
                leaderboard.addPlayer(player)
                pickle.dump(leaderboard, open('leaderboard.pickle', 'wb'))
                message = name + ' has been added to the leaderboard'
                break
    else:
        message = 'You are not permitted to use this command'
    await ctx.send(message)
                    
discBot.run(TOKEN)


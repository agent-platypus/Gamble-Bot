from horse import Horse
from leaderboard import Leaderboard
from race import Race
from decimal import Decimal
from tabulate import tabulate
import discord

def generateOpenBetsMessage(race: Race) -> str:
    message = ''
    for horse in race.horses:
        odds = (1 - horse.winProbability) / horse.winProbability
        odds = round(odds, 2)
        odds = str(odds)
        message = message + '\n' + horse.name + ': ' + odds + ':1 odds'
    return message

def generateLeaderboardMessage(leaderboard: Leaderboard) -> str:
    array = []
    for i in range(len(leaderboard.players)):
        array.append([i + 1, leaderboard.players[i].name, leaderboard.players[i].money])
    message = '```' + tabulate(array, headers=['rank', 'name', 'money']) + '```'
    return message

def generateStartRaceMesage(winner: Horse, winners: list, guild: discord.Guild) -> str:
    message = 'The race is over! The fastest horse today was ' + winner.name + '. congratulations to the winners today:'
    for tuple in winners:
        message = message + '\n' + guild.get_member(tuple[0].id).mention + ': $' + str(tuple[1])
    return message

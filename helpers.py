from race import Race
from decimal import Decimal

def generateOpenBetsMessage(race: Race) -> str:
    message = 'Bets are now open, you may bet on the following horses:'
    for horse in race.horses:
        odds = (1 - horse.winProbability) / horse.winProbability
        odds = round(odds, 2)
        odds = str(odds)
        message = message + '\n' + horse.name + ': ' + odds + ':1 odds'
    return message
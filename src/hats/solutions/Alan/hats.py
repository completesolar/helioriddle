import random

def sees(player, selections):
    ret = []
    for key in selections:
        if key==player:
            continue
        ret.append(selections[key])
    return ret

def guess(player, selections):
    playerSees = sees(player, selections)
    if player=="A":
        if "3" in playerSees and "5" in playerSees:
            return "pass"
        elif "3" in playerSees and "6" in playerSees:
            return "2"
        elif "4" in playerSees and "5" in playerSees:
            return "1"
        elif "4" in playerSees and "6" in playerSees:
            return "pass"
    elif player == "B":
        if "1" in playerSees and "5" in playerSees:
            return "pass"
        elif "1" in playerSees and "6" in playerSees:
            return "4"
        elif "2" in playerSees and "5" in playerSees:
            return "3"
        elif "2" in playerSees and "6" in playerSees:
            return "pass"
    elif player == "C":
        if "3" in playerSees and "1" in playerSees:
            return "5"
        elif "3" in playerSees and "2" in playerSees:
            return "pass"
        elif "4" in playerSees and "1" in playerSees:
            return "pass"
        elif "4" in playerSees and "2" in playerSees:
            return "6"

def didWin(guesses, selections):
    won = False
    for guess in guesses:
        if guesses[guess] == "pass":
            continue
        elif selections[guess] != guesses[guess]:
            return False
        elif selections[guess] == guesses[guess]:
            won = True
    return won

def play(players, selections):
    guesses = {}
    for player in players:
        guesses[player] = guess(player, selections)
    print guesses
    return didWin(guesses, selections)


players = []
players.append("A")
players.append("B")
players.append("C")

wins = 0
rounds = 1000
for i in xrange(rounds):
    selections = {}
    selections["A"] = str(random.randint(1,2))
    selections["B"] = str(random.randint(3,4))
    selections["C"] = str(random.randint(5,6))
    print selections
    won = play(players, selections)
    if won:
        wins += 1
    print

print 'Wins: ',wins
print 'Rounds: ',rounds
#print players
#print hats
#print selections

#print sees("A", selections)
#print sees("B", selections)
#print sees("C", selections)


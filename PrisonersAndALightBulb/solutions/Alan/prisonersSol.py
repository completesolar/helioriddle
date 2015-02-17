from random import randint

prisoners = 4
leadersCount = 0
lightOn = False
entered = [0] * prisoners
rounds = 0
while leadersCount < prisoners - 1:
    rounds+=1
    rnd = randint(0,prisoners-1)
    print rounds, rnd, lightOn, leadersCount
    if rnd == 0:
        if lightOn:
            lightOn = False
            leadersCount += 1
    else:
        if not lightOn and entered[rnd] == 0:
            lightOn = True
            entered[rnd] = 1
print "I know all prisoners have been in the lobby"

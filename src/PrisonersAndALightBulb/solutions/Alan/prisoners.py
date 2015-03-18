from random import randint

simulations = 1000
simulationCount = 0
simulationsResults = []
while simulationCount<simulations:
    prisoners = 100
    selectedArr = [0] * prisoners
    selected = 0
    days = 0
    while selected<prisoners:
        days += 1
        rnd = randint(0,prisoners-1)
        if selectedArr[rnd] == 0:
            selectedArr[rnd] = 1
            selected += 1
    print simulationCount, days
    simulationsResults.append(days)
    simulationCount += 1

print "Average: ", sum(simulationsResults) / float(simulations)
print "Min: ", min(simulationsResults)
print "Max: ", max(simulationsResults)

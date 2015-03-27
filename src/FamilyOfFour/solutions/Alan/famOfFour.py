from random import randint
twoBoysCount = 0
oneBoyCount = 0
for i in xrange(100):
    while True:
        a = randint(0,1)
        b = randint(0,1)
        if a+b > 0:
            break
    if a+b==2:
        twoBoysCount+=1
    else:
        oneBoyCount+=1

print twoBoysCount, oneBoyCount
    

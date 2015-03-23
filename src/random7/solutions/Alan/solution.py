import random

def randomFrom1To7():
    binVal = ''
    for i in xrange(3):
        while True:
         	val = random.randint(1,5)
        	if val < 5:
           		break
        if val <= 2:
        	binVal += '0'
        else:
        	binVal += '1'
    ret = int(binVal, 2)
    if ret == 0:
        return randomFrom1To7()
    return ret

# Tests

vals = []
tries = 1000
for x in xrange(tries):
	vals.append(randomFrom1To7())    
print vals
average = sum(vals) / float(tries)
# average should be around 4
print average

#the number of values in each of these arrays should be about tries / 7
sevens = [1 for x in vals if x==7]
print "7:",len(sevens)
sixes = [1 for x in vals if x==6]
print "6:",len(sixes)
fives = [1 for x in vals if x==5]
print "5:",len(fives)
fours = [1 for x in vals if x==4]
print "4:",len(fours)
threes = [1 for x in vals if x==3]
print "3:",len(threes)
twos = [1 for x in vals if x==2]
print "2:",len(twos)
ones = [1 for x in vals if x==1]
print "1:",len(ones)

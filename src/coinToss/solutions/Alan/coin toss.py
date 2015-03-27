import random

yourSeq = raw_input("What is your sequence?")
mySeq = yourSeq[0:2]
if mySeq[1] == '1':
    mySeq = '2' + mySeq
else:
    mySeq = '1' + mySeq

print "Your Seq:", yourSeq
print "My Seq:", mySeq

counter=0
curString = ''
myScore = 0
yourScore = 0
while counter<1000:
    if len(curString)<3:
        curString = curString + str(random.randint(1,2))
    else:
        curString = curString[1:] + str(random.randint(1,2))
    if curString == mySeq:
        myScore+=1
        curString = ''
    elif curString == yourSeq:
        yourScore+=1
        curString = ''
    print curString
    counter += 1
    
print "myScore:",myScore
print "yourScore:",yourScore

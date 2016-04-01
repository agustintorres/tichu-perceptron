import operator

DOG=0
JACK=11
QUEEN=12
KING=13
ACE=14
PHOENIX=15
DRAGON=16

class CardReadingException:
    pass

def translate_hand(cards):
    hand=[0 for x in range(17)]
    for card in cards:
        if (card=="Dr"):
            hand[DRAGON]=1
        elif (card=="Ph"):
            hand[PHOENIX]=1
        elif (card=="Hu"):
            hand[DOG]=1
        elif (card=="Ma"):
            hand[1]=1
        elif (card[1]=="K"):
            hand[KING]+=1
        elif (card[1]=="D"):
            hand[QUEEN]+=1
        elif (card[1]=="B"):
            hand[JACK]+=1
        elif (card[1]=="A"):
            hand[ACE]+=1
        elif (card[1]=="1"):
            hand[10]+=1
        else:
            hand[int(card[1])]+=1
    # sanity check
    sum=0
    for x in hand:
        sum+=x
    if (sum!=14):
        print cards
        print hand
        raise CardReadingException()
    
    return tuple(hand)

def loadData(dataFile):
    data=open(dataFile, "r")
    dataPoints=[]
    for line in data:
        parts=line.split(" ", 1)
        answer=False
        if (parts[0] == "TICHU"):
            answer=True
        l=eval(parts[1])
        dataPoints.append((answer, translate_hand(l)))
    return dataPoints

def dotProduct(x, y):
   return reduce(operator.add, map(operator.mul, x, y)) 

def writeModelToFile(model, fileName):
    out=open(fileName, "w")
    out.write(str(model))
    out.close()

def readModelFromFile(fileName):
    inp=open(fileName, "r")
    data=eval(inp.readline().strip())
    inp.close()
    return data

def evaluate(testFile, modelFile, predict):
    testExamples=loadData(testFile)
    model=None
    if modelFile:
        model=readModelFromFile(modelFile)
    right=0.0
    wrong=0.0
    tp=0.0
    fp=0.0
    fn=0.0
    for (answer, hand) in testExamples:
       if (answer==predict(hand, model)):
           right+=1.0
           if (answer):
               tp+=1.0
       else:
           wrong+=1.0
           if (answer):
               fn+=1.0
           else:
               fp+=1.0
    print "% correct: " + str(100.0*right/(right+wrong))
    if (tp+fp)==0:
        precision=1.0
    else:
        precision=tp/(tp+fp)
    recall=tp/(tp+fn)
    f1=2*precision*recall/(precision+recall)
    print "F1: " + str(f1)

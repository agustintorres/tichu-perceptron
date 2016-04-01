import sys
from tichu import *
exec "from " + sys.argv[1] + " import *"

def exampleFeatureFunction(hand):
    fv=[0, 0, 0]
    fv[0]=1
    if (hand[DRAGON]>0):
        fv[1]=1.0
    if (hand[PHOENIX]>0):
        fv[2]=1.0
    return fv

def dotProductPredictor(featureFunction, hand, model):
    return dotProduct(featureFunction(hand), model)>0

def exampleDotProductPredictor(hand, model):
    return dotProductPredictor(exampleFeatureFunction, hand, model)

def myDotProductPredictor(hand, model):
    return dotProductPredictor(allCombined, hand, model)

def votedPerceptronPredictor(featureFunction, hand, models):
    sum = 0
    votespro = 0
    votescon = 0
    #print "inside vp predictor"
    #print "len of models" + str(len(models))
    for i in range(len(models)):
        if ( cmp(dotProduct(featureFunction(hand), models[i]), 0) > 0 ):
          votespro += 1
        else:
          votescon +=1
    if (votespro>votescon):
        return True
    else:
        return False
    #return cmp(sum, 0)>0

def myVotedPredictor(hand, models):
    #times = readModelFromFile("allCombined.model.voted.times")
    return votedPerceptronPredictor(allCombined, hand, models)

def alwaysSayNo(hand, model):
    return False

if __name__=="__main__":
    if (sys.argv[3]=="baseline"):
        evaluate(sys.argv[2], None, alwaysSayNo)
    elif (sys.argv[3]):
        evaluate(sys.argv[2], sys.argv[3], eval(sys.argv[4]))


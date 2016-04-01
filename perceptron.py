import sys
from tichu import *
from student import *

def perceptronAlgorithm(testFile, featureFunction):
    testExamples = loadData(testFile)
    #initialize w to the correct size
    fakeHand = [0 for x in range(17)]
    fakeVector = featureFunction(fakeHand)
    w = [0 for x in range(len(fakeVector))]
    for i in range(10): # run 10 iteration of Perceptron algorithm
        for (answer, hand) in testExamples:
            if (answer):
                y = 1
            else:
                y = -1
            x = featureFunction(hand)
            y_hat = cmp(dotProduct(w, x), 0) #same as sgn(w.x, 0)
            if (y_hat != y):
                yx = [y*feat for feat in x]
                w = map(operator.add, w, yx)
    return w

def averagedPerceptron(testFile, featureFunction):
    testExamples = loadData(testFile)
    #initialize w to the correct size
    fakeHand = [0 for x in range(17)]
    fakeVector = featureFunction(fakeHand)
    w = [0 for x in range(len(fakeVector))]
    wsum = [0 for x in range(len(fakeVector))]
    for i in range(10):
        for (answer, hand) in testExamples:
            if (answer):
                y = 1
            else:
                y = -1
            x = featureFunction(hand)
            y_hat = cmp(dotProduct(w, x), 0) #same as sgn(w.x, 0)
            if (y_hat != y):
                yx = [y*feat for feat in x]
                w = map(operator.add, w, yx)
            wsum = map(operator.add, wsum, w)

    numberOfModels = 45000*10 #45k training examples over 10 iterations
    return [(1.0/numberOfModels)*elem for elem in wsum]

def votedPerceptron(testFile, featureFunction):
    testExamples = loadData(testFile)
    #initialize w to the correct size
    fakeHand = [0 for x in range(17)]
    fakeVector = featureFunction(fakeHand)
    w = [0 for x in range(len(fakeVector))]
    allmodels = [w]
    survivaltimes = [0]
    i = 0
    for i in range(10):
        for (answer, hand) in testExamples:
            if (answer):
                y = 1
            else:
                y = -1
            x = featureFunction(hand)
            y_hat = cmp(dotProduct(w, x), 0) #same as sgn(w.x, 0)
            if (y_hat != y):
                yx = [y*feat for feat in x]
                w = map(operator.add, w, yx)
                allmodels.append(w)
                survivaltimes.append(1)
                i += 1
            else:
                survivaltimes[i] += 1
    return (allmodels, survivaltimes)

def exampleFeatureFunction(hand):
    fv=[0, 0, 0]
    fv[0]=1
    if (hand[DRAGON]>0):
        fv[1]=1.0
    if (hand[PHOENIX]>0):
        fv[2]=1.0
    return fv

testFile = sys.argv[1]
featureFunction = eval(sys.argv[2])
modelFile = sys.argv[3]

averaged = False
voted = False
if (len(sys.argv) >= 5 and sys.argv[4] == "-averaged"):
    averaged = True

if (len(sys.argv) >= 5 and sys.argv[4] == "-voted"):
    voted = True

if (averaged == True):
    print "running averaged perceptron..."
    model = averagedPerceptron(testFile, featureFunction)
    print model 
    writeModelToFile(model, modelFile)
elif (voted == True):
    print "running voted perceptron..."
    all = votedPerceptron(testFile, featureFunction)
    writeModelToFile(all[0], modelFile)
    writeModelToFile(all[1], modelFile+".times")
else:
    print "running regular perceptron..."
    model = perceptronAlgorithm(testFile, featureFunction)
    print model
    writeModelToFile(model, modelFile)
    

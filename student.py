from tichu import *


def firstFeatureFunction(hand):
    fv = [0, 0, 0, 0, 0, 0]
    fv[0] = 1
    if (hand[DRAGON] > 0):
        fv[1] = 1.0
    if (hand[PHOENIX] > 0):
        fv[2] = 1.0
    if (hand[DOG] > 0):
        fv[3] = 1.01
    if (hand[1] > 0):
        fv[4] = 1.0
    if (hand[ACE] > 0):
        fv[5] = 1.0
    return fv

# 18 features: for each type 
# of card, the number of cards of that type
# that the hand contains
def numberOfCards(hand):
    fv = [0 for x in range(17)]
    for i in range(17):
        if (hand[i] > 0):
            fv[i] = hand[i]
    return fv

def numberOfEachHighCard(hand):
    fv = [0 for x in range(7)]
    
    fv[0] = hand[DRAGON]
    fv[1] = hand[PHOENIX]
    fv[2] = hand[ACE]
    fv[3] = hand[KING]
    fv[4] = hand[QUEEN]
    fv[5] = hand[JACK]
    fv[6] = hand[10]
    return fv

# 1 feature: total number
# of high cards (D, P, A, K, Q, J, and 10)
def numberOfHighCards(hand):
    fv = [0]
    fv[0] = hand[DRAGON] + hand[PHOENIX] + hand[ACE] + \
            hand[KING] + hand[QUEEN] + hand[JACK] + hand[10]
    return fv

def getNumberOfLosers(hand):
    losers = 0
    losers += hand[DOG]
    for i in (1,2,3):
        if (hand[i] <= 3):
            losers += hand[i]
    for i in (4,5):
        if (hand[i] <= 2):
            losers += hand[i]
    return [losers]

def getNumberOfMiddles(hand):
    middles = 0
    middles += hand[6] + hand[7] + hand[8] + hand[9] + hand[10] 
    for i in (JACK, QUEEN):
        if (hand[i] <= 2):
            middles += hand[i]
    return [middles]

def getNumberOfWinners(hand):
    winners = 0
    #high singletons
    winners += hand[DRAGON] + hand[PHOENIX]
    #high groups
    for i in (JACK,QUEEN,KING,ACE):
        if (hand[i] >= 2):
            winners += hand[i]
    if (hasStraight(hand)):
        winners += 1
    if (hasFullHouse(hand) and numberOfHighTriples(hand)>0):
        winners += 1
    return [winners]

def getNumberOfAces(hand):
    return [hand[ACE]]

def hasPair(hand):
    pair = False
    for i in range(17):
        if (hand[i] >= 2):
            pair = True
            break
    if (pair):
	return [1.0]
    else: 
	return [0.0]

def hasTriple(hand):
    triple = False
    for i in range(17):
        if (hand[i] >= 3):
            triple = True
            break
    if (triple):
	return [1.0]
    else: 
	return [0.0]

def hasConsecutivePairs(hand):
    hasconpair = False
    for i in range(17):
        if (hasconpair):
            break
        currlen = 0
        for j in range(i, 17):
            if (currlen >= 2):
                hasconpair = True
                break
            if (hand[j] >= 2):
                currlen += 1
            else:
                break
    if (hasconpair):
	return [1.0]
    else:
        return [0]

def lengthOfLargestConsecPair(hand):
    if (hasConsecutivePairs(hand) == [0]):
        return [0]
    maxlen = 0
    for i in range(17):
        currlen = 0
        for j in range(i, 17):
            if (hand[j] >= 2):
                currlen += 1
                if (currlen > maxlen):
                    maxlen = currlen
            else:
                break
    return [maxlen]

def hasFullHouse(hand):
    hasPair = False
    hasTriple = False
    pos = -1
    for i in range(17):
        if (hand[i] == 2):
            hasPair = True
            pos = i
    for i in range(17):
        if ( (i != pos) and (hand[i] == 3) ):
            hasTriple = True
    if (hasPair and hasTriple):
	return [1.0]
    else:
	return [0]

def hasStraight(hand):
    straight = False
    for i in range(17):
        if straight:
            break
        currlen = 0
        for j in range(i, 17):
            if (currlen >= 5):
                straight = True
                break
            if (hand[j] >= 1):
                currlen += 1
            else:
                break
    if (straight):
	return [1.0]
    else:
        return [0]

def lengthOfBiggestStraight(hand):
    if (hasStraight(hand) == [0]):
        return [0]
    maxlen = 0
    for i in range(17):
        currlen = 0
        for j in range(i, 17):
            if (hand[j] >= 1):
                currlen += 1
                if (currlen > maxlen):
                    maxlen = currlen
            else:
                break
    return [maxlen]

def numberOfCardsLessThanFour(hand):
    count = 0
    for i in range(1,5):
        count += hand[i]
    return [count]

def acesMinusFours(hand):
    return [getNumberOfAces(hand)[0] - numberOfCardsLessThanFour(hand)[0]]


# 1 feature: 1 if it's a 'good' hand
# ie, more winners than losers
def internetArticle(hand):
    fv = [0]
    winners = getNumberOfWinners(hand)
    middles = getNumberOfMiddles(hand)
    losers = getNumberOfLosers(hand)
    if (winners[0] > (losers[0]+middles[0])):
        fv[0] = 1.0
    return fv

def hasPhoenix(hand):
    return [hand[PHOENIX]]

def hasDragon(hand):
    return [hand[DRAGON]]

def hasMa(hand):
    return [hand[1]]

def hasDog(hand):
    return [hand[DOG]]

def averageValueOfHand(hand):
    count = 0
    for i in range(17):
        count += hand[i]*i
    return [count*1.0/18]

#average of Losers, Middles, and Winners
def averageOfLMD(hand):
    winners = getNumberOfWinners(hand)
    middles = getNumberOfMiddles(hand)
    losers = getNumberOfLosers(hand)
    return [(winners[0]+middles[0]+losers[0])*1.0/18]

#def minSingle(hand)

#def maxSingle(hand)

def hasPhoenixAndDragon(hand):
    if (hand[PHOENIX]>0 and hand[DRAGON]>0):
        return [1.0]
    else:
        return [0]

def getNumberOfSpecialCards(hand):
    return [hand[DOG] + hand[DRAGON] + hand[PHOENIX] + hand[1]]

def numberOfHighPairs(hand):
    count = 0
    for i in (10,JACK,QUEEN,KING,ACE):
        if (hand[i] >= 2):
            count += 1
    return [count]

def numberOfHighTriples(hand):
    count = 0
    for i in (10,JACK,QUEEN,KING,ACE):
        if (hand[i] >= 3):
            count += 1
    return [count]

def numberOfSingles(hand):
    count = 0
    for i in range(17):
        if (hand[i] == 1):
            count += 1
    return [count]

def allCombined(hand):
    w1 = firstFeatureFunction(hand) 
    w2 = numberOfCards(hand)
    w3 = numberOfEachHighCard(hand)
    w4 = numberOfHighCards(hand)
    w5 = getNumberOfLosers(hand)
    w6 = getNumberOfMiddles(hand)
    w7 = getNumberOfWinners(hand)
    w8 = getNumberOfAces(hand)
    w9 = hasPair(hand)
    w10 = hasTriple(hand)
    w11 = hasConsecutivePairs(hand)
    w12 = lengthOfLargestConsecPair(hand)
    w13 = hasFullHouse(hand)
    w14 = hasStraight(hand)
    w15 = lengthOfBiggestStraight(hand)
    w16 = acesMinusFours(hand)
    w17 = internetArticle(hand)
    w18 = hasPhoenix(hand)
    w19 = hasDragon(hand)
    w20 = hasMa(hand)
    w21 = hasDog(hand)
    w22 = averageValueOfHand(hand)
    w23 = averageOfLMD(hand)
    w24 = hasPhoenixAndDragon(hand)
    w25 = getNumberOfSpecialCards(hand)
    w26 = numberOfHighPairs(hand)
    w27 = numberOfHighTriples(hand)
    w28 = numberOfSingles(hand)
    #return w2+w4+w8+w10+w11+w12+w13+w14+w15+w16+w18+w19+w22+w23+[1]
    #return [1]+w2+w10+w11+w13+w14+w15+w16+w17+w18+w19+w22+w24
    #return w2+w3+w4+w5+w6+w7+w8+w25
    return w1+w2+w3+w4+w5+w6+w7+w8+w9+w10+w11+w12+w13+w14+w15+w16+w17+w18+w19+w20+w21+w22+w23+w24+w25+w26+w27+w28

    



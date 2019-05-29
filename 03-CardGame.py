# This game works like this.
# 2 players - each dealt 5 cards.
# both player flip the first card at the same time.
# The player with the even number gets to keep the score while the player with odd number discards the card.
# From then on, cards are flipped. Even numbers are added to the score. Odd numbers are subtracted.
# At the end, the scores are tallied and the player with the higher score wins

import random

def generateRandomNumber():
    return random.randint(1,10)

def processCard(card):
    if (card % 2 == 0):
        print(f"Card: {card} is Even. Add it")
        score = card
    else:
        print(f"Card: {card} is Odd. Subtract it")
        score = card * -1
    return score

# Setup
player1cards = []
player2cards = []
p1score = 0
p2score = 0
noOfCards = 5
for i in range(noOfCards):
    player1cards.append(generateRandomNumber())
    player2cards.append(generateRandomNumber())

#Start playing
for currCard in range(noOfCards):
    print(f"Current Card No: {currCard+1}")

    # First card warrants special processing
    if currCard == 0: #First card is marked at array index 0
        p1card = player1cards[currCard]
        p2card = player2cards[currCard]
        score = processCard(p1card)
        if (score >= 0):
            p1score = p1score + score
            print (f"Player1 First Card is {p1card} is even. Score = {p1score}")
        else:
            print (f"Player1 First Card is {p1card} is odd. Score = {p1score}")

        score = processCard(p2card)
        if (score >= 0):
            p2score = p2score + score
            print (f"Player2 First Card is {p2card} is even. Score = {p2score}")
        else:
            print (f"Player2 First Card is {p2card} is odd. Score = {p2score}")

    # Not the first card
    else:
        p1card = player1cards[currCard]
        p2card = player2cards[currCard]

        p1score = p1score + processCard(p1card)
        p2score = p2score + processCard(p2card)
        print (f"Player1 Card is {p1card}. Score = {p1score}")
        print (f"Player2 Card is {p2card}. Score = {p2score}")

    print("Next Draw...\n")
#Print results
print(f"Player 1 cards: {player1cards}")
print(f"Player 2 cards: {player2cards}")
print(f"Player 1 score: {p1score}")
print(f"Player 2 score: {p2score}")
if (p1score > p2score):
    print("Player 1 wins!\a")
elif (p2score > p1score):
    print("Player 2 wins!\a")
else:
    print("Its a tie!\a\a")

# This is a module used by ex40-modulevsclass.py
import random

favourite_fruit = "Tangerine"

def getARandomFruit():
    fruits = ['Apples','Oranges','Pears','Grapes']
    return fruits[random.randint(0,len(fruits)-1)]


# print (getARandomFruit())

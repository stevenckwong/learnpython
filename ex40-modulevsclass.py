# Shows the difference between modules and class
import ex40module
import random

# Module
print (f"Favourite fruit is {ex40module.favourite_fruit}")
print (f"A random fruit is {ex40module.getARandomFruit()}")
ex40module.favourite_fruit = "Bananas"
print (f"Favourite fruit is {ex40module.favourite_fruit}")
# #The above shows that there is only 1 module. when the module variable is updated, it is updated for everyone

# Class
class FruitLover(object):
    favourite_fruit = "Bananas"
    my_fruits = ['Apples','Oranges','Pears','Grapes']
    def __init__(self,favfruit):
        self.favourite_fruit = favfruit

    # Notice that when declaring a method, you must always have the self passed in.
    # referencing the attributes must be done using the self
    def getARandomFruit(self):
        return self.my_fruits[random.randint(0,len(self.my_fruits)-1)]

##################################

bananaLover = FruitLover("Bananas")
durianLover = FruitLover("Durians")

print (f"BananaLover loves {bananaLover.favourite_fruit}")
print (f"DurianLover loves {durianLover.favourite_fruit}")
print (f"BananaLover occasionally eats {bananaLover.getARandomFruit()}")
print (f"DurianLover occasionally eats {durianLover.getARandomFruit()}")
bananaLover.favourite_fruit = bananaLover.getARandomFruit();
print (f"Something happened and BananaLover now loves {bananaLover.favourite_fruit}")
print (f"But DurianLover still loves {durianLover.favourite_fruit}")

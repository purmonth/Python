import numpy as np
import pulp
##from coinor.pulp import *


myList = ['apple', 'orange', 'banana'] 
myDict = {'apple':'red', 'orange':'orange', 'banana':'yellow'} 
print(myList[0]) ## Displays "apple" 
print(myDict['apple']) ## Displays "red"


even = [i for i in [1,2,3,4,5,6,7,8,9] if i%2 == 0]
print(even)

REQUIRE = { 
    1 : 7, 
    2 : 5, 
    3 : 3, 
    4 : 2, 
    5 : 2 
} 
PRODUCTS = [1, 2, 3, 4, 5] 
LOCATIONS = [1, 2, 3, 4, 5] 
CAPACITY = 8
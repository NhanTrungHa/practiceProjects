#make a 10x loop
# store random one through 9 into two variables

#keep track of points

# keep track of errors

# break if errors > 3 each loop
#8 second time limit
import random
import sys
import time
points = 0

for i in range(10):
    digitOne = random.randrange(0, 9)
    digitTwo = random.randrange(0, 9)
    product = digitOne * digitTwo

    for tries in range(0, 3):
        totalTries = 3 - tries
        answer = input("%s * %s = " % (digitOne, digitTwo))
        if int(answer) == product:
            points += 1
            print("Correct! Points: %s" % points)
            break
        print("wrong. Tries left: %s" % totalTries)







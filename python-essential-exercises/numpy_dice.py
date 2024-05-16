# Import numpy as np
import numpy as np 
import time

# Set the dynamic seed
np.random.seed(int(time.time()))

# Starting step
step = 50

# Generate and print random float
#print(np.random.rand())

# Use randint() to simulate a dice and Roll the dice
dice = np.random.randint(1, 7)

# Finish the control construct
if dice <= 2 :
    step -= 1
elif dice == 1 or dice == 2 :
    step -= np.random.randint(1,7)
else :
    step += np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)
# Import numpy as np
import numpy as np 
import time
import matplotlib.pyplot as plt

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

# Initialize random_walk
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        # Replace below: use max to make sure step can't go below 0
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

print(random_walk)

# Plot random_walk
plt.plot(random_walk)
plt.show()

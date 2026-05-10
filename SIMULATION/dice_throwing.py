import random
import numpy as np
from collections import Counter

n_sims = 1000
dice_nums = [1, 2, 3, 4, 5, 6]

dice_1 = []
dice_2 = []

for i in range(0, n_sims):
    dice_1.append(random.choice(dice_nums))
    dice_2.append(random.choice(dice_nums))

result = np.array(dice_1) + np.array(dice_2)
counts = Counter(result)

# print the dice sum number and their instance
for num, count in counts.most_common():
    percentage = count/n_sims
    print(f"Dice Sum:{num}, Number of Counts : {count}, Percentage : {percentage}")



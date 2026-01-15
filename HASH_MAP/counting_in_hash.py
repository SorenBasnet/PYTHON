"""
Want to count and want to use hash while counting ? 
"""


winners = ["brazil", "brazil", "england", "USA"]

count = {}

for team in winners: 
    count[team] = count.get(team, 0) + 1

print(count)



# Even better 
from collections import Counter 

print(Counter(winners))
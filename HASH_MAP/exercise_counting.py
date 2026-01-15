""" 
count the number of wins of team 
"""

from collections import Counter

wc_winner = {
    "brazil" : [1999, 2000], 
    "england" : [2000]
}

count={}


for team in wc_winner: 
    count[team] = (len(wc_winner[team]))


print(count)


# Clean up version - GPT 

wins_per_team = {}

for team, years in wc_winner.items(): 
    wins_per_team[team] = len(years)

print(wins_per_team)


print(wc_winner.items())
# Output : dict_items([('brazil', [1999, 2000]), ('england', [2000])])




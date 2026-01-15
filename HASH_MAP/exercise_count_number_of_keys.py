"""
Given the number of wc winners, count the number of years 
"""

from collections import Counter 

wc_winner = {
    "brazil" : [1999, 2000], 
    "england" : [2000]
}

year_count = Counter() 

for years in wc_winner.values():
    year_count.update(years)

print(year_count)

# But i want to do it without the collections 

year_count = {}

for years in wc_winner.values(): 
    print(years)
    for i in range (0, len(years)): 
        year = years[i]

        if year in year_count:
            year_count[year] += 1
        else:
            year_count[year] = 1

print(year_count)

# A little more pythonic : 

year_count = {}

for years in wc_winner.values():
    for year in years:
        if year in year_count:
            year_count[year] += 1
        else:
            year_count[year] = 1



# Pro pattern using .get() (still no collections)

year_count = {}

for years in wc_winner.values():
    for year in years:
        year_count[year] = year_count.get(year, 0) + 1
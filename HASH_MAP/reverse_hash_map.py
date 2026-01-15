""" 
reverse a dictonary: 

wc_winners = {
'brazil' : [1999], 
'england' : [1999, 2000]}

into something like : 

{
  1999: ["brazil"],
  2000: ["brazil", "england"]
}

"""



wc_winner = {
    "brazil": [1999, 2000], 
    "england": [2000]
}

count_year = {}

for team, years in wc_winner.items():
    for year in years:

        # create list if year not seen
        if year not in count_year:
            count_year[year] = []

        # NOW append
        count_year[year].append(team)

print(count_year)





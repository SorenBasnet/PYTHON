"""
In Python, a hash map = dictionary (dict)
"""

# Has map stores key -> value pairs 

"""
Look up by key is 0(1)
"""


# Basic syntax 

student_age = {
    "soren": 24,
    "amy": 24, 
    "sakura": 20
}

print(student_age["soren"]) #24

# Add update the dict 

student_age['lisa'] = 55 # add
student_age['soren'] = 70 # updates 


# if you try to access bob who is not in the dic 

print(student_age['bob']) # Python will crash and will have a KeyError:'bob'


# Safe look up 

student_age.get("bob", "not found")

# add value when the values are a list 

"""


if key not in d:
    d[key] = []       # create a new list for this key if it doesn’t exist

d[key].append(value)  # add the value to the list for that key


"""



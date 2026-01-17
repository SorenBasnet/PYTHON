# Real world example 

# A very common use for map() is converting a list of string
# ( like from a user input ) into integers. 

user_input = ["1", "2", "3", "4"]

# Conver all strings to integers instantly 
clean_data = list(map(int, user_input))

print(clean_data)

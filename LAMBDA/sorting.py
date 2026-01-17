"""
Imagine you have a list of names, 
and you want to sort them by the length of the name, 
not alphanetically

"""

names = ["Leonardo", "Don", "Raphael", "Mickey"]

names.sort(key=lambda name: len(name))

print(names) # Output: ['Don', 'Mikey', 'Raphael', 'Leonardo']


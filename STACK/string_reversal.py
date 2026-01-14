"""
String reversal using stack 
"""

def reverse_string(text: str) -> str: 

    stack = []

    # Push all characters onto the stack 

    for char in text:
        stack.append(char)

    reversed_text = ""

    #Pop characters until the stack is empty 
    while len(stack) > 0: 
        reversed_text += stack.pop()

    return reversed_text


print(reverse_string("apple"))



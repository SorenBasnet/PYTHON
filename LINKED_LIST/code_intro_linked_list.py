"""
In a Linked List, we need two things: a class for the Node itself and a class for the LinkedList to manage those nodes
"""

class Node: 

    def __init__(self, data): 
        self.data = data # the value 
        self.next = None # Pointer to the next node (starts as empty)


# Linked List Class 

# This class manages the "Head" of the list and 
# contains methods to add data 

class LinkedList: 

    def __init__(self): 
        self.head = None # The list starts empty 

    # Adding a node to the end ( Append )

    def append(self, data): 

        new_node = Node(data)

        # if the list is empty, make this the head 

        if not self.head: 
            self.head = new_node 
            return 
        
        # Otherwise, walk to the end of the list 

        current = self.head 

        while current.next: 
            current = current.next 

        # Point the last node to our new node 
        current.next = new_node 

    def delete(self, key): 

        current = self.head

        if current is None: 
            return 
        
        #2. If the head node itself holds the key to be deleted 

        if current.data == key: 
            self.head = current.next # the second node becomes the head 
            current = None # Free up the memory 
            return 
        
        #3. Search for the key to be deleted, keep track of the PREVIOUS node 
        prev = None 
        while current and current.data != key: 
            prev = current 
            current = current.next 

        
        # If the key was not present in the list 
        if current is None: 
            print(f"Value '{key}' not found in the list.")

            return 


        # Unline the node from the linked list 
        prev.next = current.next
        current = None         



    
    def display(self): 
        current = self.head 
        elements = []
        while current: 
            elements.append(str(current.data))
            current = current.next

        print(" -> ".join(elements) + " -> None")


        # Create a new list
my_list = LinkedList()

# Add some data
my_list.append("Apples")
my_list.append("Bananas")
my_list.append("Cherries")

# Show the result
my_list.display()

# Delete "Bananas"
my_list.delete("Bananas")

print("After deleting Bananas:")
my_list.display() # Apples -> Cherries -> None
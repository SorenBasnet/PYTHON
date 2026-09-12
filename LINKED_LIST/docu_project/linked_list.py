
class Node:

    def __init__(self, data, hault:list, blockade:bool):
        self.data = data
        self.hault : list = hault # will contain all the primary key names of other nodes. if hault is len > 0, all othe rprocesses for the person_id ( from the processes dictionary, will be haulted)
        self.next = None
        self.blockade = blockade

        if len(hault) > 0:
            pass
            # look through all the process and blockade = True all the processes, therefore, nothing can move forward.


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node


    def delete(self, key):
        current = self.head

        if current is None:
            return

        if current.data == key:
            self.head = current.next

            current = None
            return

        prev = None

        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            print(f"Value '{key}' not found in the list.")

            return

        prev.next = current.next
        current = None


    def display(self):

        current = self.head
        elements = []

        while current:
            elements.append(str(current.data))
            current = current.next

        print(" --> ".join(elements) + " --> None")





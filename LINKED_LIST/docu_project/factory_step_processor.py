

class Factory:

    def __init__(self):
        pass

    def process_pipeline(self, process):

        current = process.head

        while current is not None:
            self.process_node(current)

            if current.blockade == True:
                print("Help, the process will have to hault")
                break

            current = current.next

    def process_node(self, node):
        print(node.data)



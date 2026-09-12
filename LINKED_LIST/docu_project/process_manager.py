from linked_list import LinkedList

class Process_Manager:

    def __init__(self, filename_process="processes.json"):
        self.filename_process = filename_process
        self.process = {}

    def create_process(self, process_id):
        self.process[process_id] = LinkedList()
        print(f"Process ID : {process_id} initialized.")

    def get_process(self, process_id):
        return self.process.get(process_id)

    def delete_process(self, filename_process):
        pass

    def modify_process(self, filename_process):
        pass

    def save_process(self, filename_process):
        pass

    def load_process(self, filename_process):
        pass





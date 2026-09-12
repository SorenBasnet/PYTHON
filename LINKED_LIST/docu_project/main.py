from process_manager import Process_Manager
from factory_step_processor import Factory

def main():

    process_1 = Process_Manager()
    process_1.create_process('123')
    process_1.get_process('123').append("A")
    process_1.get_process('123').append("B")
    process_1.get_process('123').append("C")
    process_1.get_process('123').append("D")
    process_1.get_process('123').display()

    factory = Factory()
    factory.process_pipeline(process_1.get_process('123'))







if __name__=="__main__":
    main()

import multiprocessing
import time
def funktio1():
    name = multiprocessing.current_process().name
    print (name, 'is starting')
    time.sleep(1)
    print (name, 'Exiting')
    time.sleep(1)
    return
def funktio2():
    while True:
        name = multiprocessing.current_process().name
        print (name, 'is starting')
        time.sleep(1)
        print (name, 'Exiting')
        time.sleep(1)
if __name__ == '__main__':
    service1 = multiprocessing.Process(name='LÄMPÖTILANMITTAUS', target=funktio1)
    service2 = multiprocessing.Process(name='KOSTEUSMITTAUS', target=funktio2)
    service3 = multiprocessing.Process(name='ILMANPAINEENMITTAUS', target=funktio1)
    #service3 = multiprocessing.Process(target=funktio1) # use default name
    service3.start() #ILMANPAINEENMITTAUS
    time.sleep(1)
    service2.start() #KOSTEUSMITTAUS
    time.sleep(1)
    service1.start() #LÄMPÖTILANMITTAUS
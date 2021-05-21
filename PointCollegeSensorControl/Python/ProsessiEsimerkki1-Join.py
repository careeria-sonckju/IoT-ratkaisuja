from multiprocessing import Process
import time
#http://zetcode.com/python/multiprocessing/ 
def fun(val):

    print(f'Aloitetaan funktio fun {val} ')
    time.sleep(val)
    print(f'Lopetetaan funktio fun {val} ')

def main():
    print('starting main-program')
    p1 = Process(target=fun, args=(1, ))
    p1.start()
    #p1.join() #When we comment out the join method, the main process finishes before the child process.

    p2 = Process(target=fun, args=(2, ))
    p2.start()
    #p2.join()

    p3 = Process(target=fun, args=(3, ))
    p3.start()
    #p3.join()

    p1.join()
    p2.join()
    p3.join()

    print('finished main')

if __name__ == '__main__':

    main()
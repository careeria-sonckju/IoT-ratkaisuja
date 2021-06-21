import multiprocessing
import time
import os #pid:iä varten!
#tring formatting = https://www.learnpython.org/en/String_Formatting
queue1 = multiprocessing.Queue()
queue2 = multiprocessing.Queue()
def ProsessiFunktio1(que):
    while True:
        while not que.empty():
            event = que.get()
        print ('Isäntäprosessin pid=%d ja aliprosessin pid=%d ja työvaihe=%s' % (os.getppid(), os.getpid(), event))
        time.sleep(1)
def main():
    queue1.put("initializing1")
    queue2.put("initializing2")
    p1 = multiprocessing.Process(target=ProsessiFunktio1, args=(queue1,))
    p1.start()
    p2 = multiprocessing.Process(target=ProsessiFunktio1, args=(queue2,))
    p2.start()
    time.sleep(7)
    kierros=0
    while True:
        kierros +=1
        strKierros = str(kierros)
        queue1.put(strKierros)
        queue2.put(strKierros)
        time.sleep(1)

if __name__ == '__main__':
    main()
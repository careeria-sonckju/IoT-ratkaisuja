import multiprocessing
import time
import os #pid:iä varten!
#tring formatting = https://www.learnpython.org/en/String_Formatting
def ProsessiFunktio(num):
    print ('Käynnistetään prosessi numero =', num)
    print ('Isäntäprosessin pid=%d ja aliprosessin pid=%d ' % (os.getppid(), os.getpid()))
    return

if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=ProsessiFunktio, args=(i,))
        p.start()
        time.sleep(1)
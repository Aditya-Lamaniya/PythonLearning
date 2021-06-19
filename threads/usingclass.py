from threading import *
from time import sleep
class Mythread():
    def dspnum(self):
        i=0
        print(current_thread().getName())
        sleep(1)
        while(i<=10):
            print(i)
            i+=1

obj=Mythread()
t=Thread(target=obj.dspnum)
t.start()

# multithreading
t1=Thread(target=obj.dspnum)
t1.start()

t2=Thread(target=obj.dspnum)
t2.start()
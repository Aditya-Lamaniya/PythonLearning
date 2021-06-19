import random
import time
from threading import *
import queue

def producer(q):
      while True:
        print('producing')
        q.put(random.randint(1, 50))
        print(' produced ')
        time.sleep(2)


def consumer(q):
    while True:
        print(' ready for consumption')
        print(' consume data :', q.get())
        time.sleep(2)


q = queue.Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))

t1.start()
t2.start()

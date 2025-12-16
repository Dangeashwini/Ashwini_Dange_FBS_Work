from threading import Thread,Lock
import time
import random

buffer=[]
buffer_size=5
lock=Lock()

def producer(name):
    while(True):
        item=random.randint(1,100)
        lock.acquire()
        if(len(buffer)<buffer_size):
            buffer.append(item)
            print(f"Producer {name} produced: {item} Buffer: {buffer}")
        lock.release()
        time.sleep(1)
        
def consumer(name):
    while(True):
        lock.acquire()
        if(len(buffer)>0):
            item=buffer.pop(0)
            print(f"consumer {name} consumed: {item} Buffer: {buffer}")
        lock.release()
        time.sleep(1)

t1=Thread(target=producer,args=("p1",))
t2=Thread(target=producer,args=('p2',))
t3=Thread(target=consumer,args=('c1',))
t4=Thread(target=consumer,args=('c2',))
t1.start()
t2.start()
t3.start()
t4.start()

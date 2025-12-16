from threading import Thread,Lock
import time
lock=Lock()
turn='upper'
def uppercase():
    global turn
    for i in range(65,91):
        while(True):
            lock.acquire()
            if(turn=='upper'):
                print(chr(i),end=' ')
                
                time.sleep(1)
                turn='lower'
                lock.release()
                break
            lock.release()
def lowercase():
    global turn
    for i in range(97,123):
        while(True):
            lock.acquire()
            if(turn=='lower'):
                print(chr(i),end=' ')
                time.sleep(1)
                turn='upper'
                lock.release()
                break
            lock.release()



t1=Thread(target=uppercase)
t2=Thread(target=lowercase)
t1.start()
t2.start()
t1.join()
t2.join()
        
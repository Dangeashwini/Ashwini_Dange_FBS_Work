from threading import Thread,Lock
import time
lock=Lock() 
turn='odd'    
def oddNum():
    global turn
    for i in range(1,11,2):
        while(True):
            lock.acquire()
            if(turn=='odd' and i%2!=0):
            
                    print(i,end='')
                    time.sleep(1)
                    turn='even'
                    lock.release()
                    break
            lock.release()
                
def evenNum():
    global turn
    for i in range(2,11,2):
        while(True):
            
            lock.acquire()
            if(turn=='even' and i%2==0):
                print(i,end='')
                time.sleep(1)
                turn='odd'
                lock.release()
                break
                    
            lock.release()

    

t1=Thread(name='Thread1',target=oddNum)
t2=Thread(name='Thread2',target=evenNum)
t1.start()
t2.start()
t1.join()
t2.join()
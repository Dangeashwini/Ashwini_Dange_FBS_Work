from threading import Thread
result=[0,0,0,0]
def sum1():
    total=0
    for i in range(1,26):
        total+=i*i
    result[0] = total
def sum2():
    total=0
    for i in range(26,51):
        total+=i*i
    result[1] = total

def sum3():
    total=0
    for i in range(51,76):
        total+=i*i
    result[2] = total

def sum4():
    total=0
    for i in range(76,101):
        total+=i*i
    result[3] = total
t1=Thread(name='Thread1',target=sum1)
t2=Thread(name='Thread2',target=sum2)
t3=Thread(name='Thread3',target=sum3)
t4=Thread(name='Thread4',target=sum4)
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
print(f"final sum is {sum(result)}")
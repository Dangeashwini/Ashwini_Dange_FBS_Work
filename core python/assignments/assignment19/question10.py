def Range(start,stop,step=1):
    if step==0:
        print("step should not 0")
    
        
    if step>0:
        while(start<stop):
            yield start
            start+=step
    else:
        while(start>stop):
            yield start
            start+=step

for i in Range(1,10):
    print(i)

    
    
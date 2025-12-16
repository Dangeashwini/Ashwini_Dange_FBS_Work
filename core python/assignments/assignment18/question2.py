class Distance:
    def __init__(self,km,m,cm):
        self.km=km
        self.m=m
        self.cm=cm
        
    def __del__(self):
        print("Inside destuctor..")
        
    def __add__(self,other):
        cm=self.cm+other.cm
        m=cm//100
        cm=cm%100
        m=self.m+other.m+m
        km=m//1000
        m=m%1000
        km=self.km+other.km+km
        return f"{km}:{m}:{cm}"
        
    
    def __sub__(self,other):
        cm=self.cm-other.cm
        m=cm//100
        cm=cm%100
        m=self.m-other.m-m
        km=m//1000
        m=m%1000
        km=self.km-other.km-km
        return f"{km}:{m}:{cm}"
        
    
obj1=Distance(1,2500,14000)
obj2=Distance(3,1400,32000)

print(obj1+obj2) 
print(obj1-obj2)       
    
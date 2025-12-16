class Shirt:
    size_price={'small':0,'medium':10,'large':20,'xlarge':30}
    def __init__(self,sid,sname,type,price,size):
        self.SID=sid
        self.SName=sname
        self.type=type
        self.price=price
        self.size=size
    
    def __del__(self):
        print("Inside desctructor..")
        
    def ShowShirt(self):
        print(f"{self.SID}, {self.SName}, {self.type}, {self.price}, {self.size}")
        final_price=self.price*(1+Shirt.size_price.get(self.size)/100)
        print(final_price)
        
    
s1 = Shirt(1, "Formal Shirt", "Formal", 1000, "small")
s1.ShowShirt()

s2 = Shirt(1, "Formal Shirt", "Formal", 1000, "medium")
s2.ShowShirt()

s3 = Shirt(1, "Formal Shirt", "Formal", 1000, "large")
s3.ShowShirt()

s4 = Shirt(1, "Formal Shirt", "Formal", 1000, "xlarge")
s4.ShowShirt()
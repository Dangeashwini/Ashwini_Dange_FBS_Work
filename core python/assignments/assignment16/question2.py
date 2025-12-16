class Product:
    discount=0
    def __init__(self,pid,pname,price,quantity):
        self.PID=pid
        self.PName=pname
        self.price=price
        self.quantity=quantity
        Product.discount=10
        
        
    def __del__(self):
        print("Inside destructor..")
        
    def ShowProduct(self):
        print(f"{self.PID},{self.PName},{self.price},{self.quantity}")
        print(f"price after {self.discount}% disc:{self.discountPrice()}")
        
   
    def discountPrice(self):
        return self.price*(1-Product.discount/100)

p1=Product(1,'washing powder',100,'2kg')
p1.ShowProduct()
    
        

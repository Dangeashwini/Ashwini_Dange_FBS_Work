class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.img=imag

    def __del__(self):
        print("This is destuctor")

    def __add__(self,other):
        return Complex(self.real+other.real,self.img+other.img)

    def __sub__(self,other):
        return Complex(self.real-other.real,self.img-other.img)
    
    def __str__(self):
        return f"{self.real} + {self.img}i"

c1=Complex(3,4)
c2=Complex(1,2)
print(c1+c2)
print(c1-c2)




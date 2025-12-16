class Book:
    count=0
    def __init__(self,bid,bname,price,author):
        self.BID=bid
        self.BName=bname
        self.price=price
        self.author=author
        Book.count+=1
        
    def __del__(self):
        print("This is destructor..")
        
    def ShowBook(self):
        print(f"{self.BID} {self.BName} {self.price} {self.author}")
        
b1=Book(1,'c programing','500','Yashvant Kanetkar')
b1.ShowBook()

        
b2=Book(1,'c programing','500','Yashvant Kanetkar')
b2.ShowBook()

print(Book.count)

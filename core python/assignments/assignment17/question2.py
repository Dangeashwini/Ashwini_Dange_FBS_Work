from question1 import Student

class EnggStudent(Student):
    def __init__(self,StudentID=2,Name='Ash',Age=23,Percentage=45,Branch='Computer',InternalMarks=40):
        super().__init__(StudentID,Name,Age,Percentage)
        self.br=Branch
        self.Imarks=InternalMarks
        
    def Display(self):
        super().Display()
        print("Branch:",self.br)
        print("Internal Marks:",self.Imarks)
        
    def Accept(self):
        super().Accept()
        self.br=input("Enter branch of student:")
        self.Imarks=int(input("Enter internal marks of student: "))
        
    def __str__(self):
        print("Inside str method")
# obj2=EnggStudent()
# obj2.Accept()
# obj2.Display()

        
        

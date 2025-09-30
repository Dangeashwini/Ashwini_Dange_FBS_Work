from question2 import Student
class MedicalStudent(Student):
    def __init__(self,StudentID=1,Name='PQR',Age=18,Percentage=89,Specialization='Zoology',MarksOfInternship=80):
        super().__init__(StudentID,Name,Age,Percentage)
        self.specialization=Specialization
        self.mOfInternship=MarksOfInternship
        
    def Display(self):
        super().Display()
        print("Specialization:",self.specialization)
        print("Internship Marks:",self.mOfInternship)
        
    def Accept(self):
        super().Accept()
        self.specialization=input("Enter specialization of student:")
        self.mOfInternship=int(input("Enter internship marks of student: "))
    
    def __str__(self):
        print("Inside str method")
        
# obj1=MedicalStudent()
# obj1.Accept()
# obj1.Display()

    
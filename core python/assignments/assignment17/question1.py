class Student:
    def __init__(self,StudentID=1,Name='ABC',Age=23,Percentage=35):
        self.sID=StudentID
        self.nm=Name
        self.age=Age
        self.per=Percentage
        
    def Display(self):
        print("Student ID:",self.sID)
        print("Student Name:",self.nm)
        print("Age:",self.age)
        print("Percentage:",self.per)
    
    def Accept(self):
        self.sID=int(input("Enter student id:"))
        self.nm=input("Enter name of student:")
        self.age=int(input("Enter age of student: "))
        self.per=int(input("Enter percentage of student:"))
        
    def calculateRank(self):
        if(self.per)>=90 and (self.per)<=100:
            print("First Rank")
        elif(self.per)>=70 and (self.per)<90:
            print("Second Rank")
        elif(self.per)>=50 and (self.per)<70:
            print("Third Rank")
        elif(self.per)>=35 and (self.per)<50:
            print("Fourth Rank")
        elif(self.per)>=1 and (self.per)<35:
            print("Fail")
        else:
            print("Invalid Percenatge")
    def __str__(self):
        print("Inside str method")
         
# obj1=Student()
# obj1.Accept()
# obj1.Display()
# obj1.calculateRank()
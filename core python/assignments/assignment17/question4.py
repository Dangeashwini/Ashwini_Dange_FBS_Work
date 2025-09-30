class College:
    def __init__(self,max_students):
        self.max_students=max_students
        self.students=[]
        
    def AddStudent(self,roll_no,name,age,marks):
        if len(self.students)>=self.max_students:
            print("Cannot add more students")
            return
        for i in self.students:
            if i["roll_no"]==roll_no:
                print("Student with this roll no {roll_no} already exists")
                return 
        self.students.append({"roll_no":roll_no,"name":name,"age":age,"marks":marks})
        print(f"Student {name} added successfully")
        
                
    def GetStudent(self,roll_no):
        for i in self.students:
            if i["roll_no"]==roll_no:
                return i
        # return None
    
    def RemoveStudent(self,roll_no):
        for i in self.students:
            if i["roll_no"]==roll_no:
                self.students.remove(i)
                print(f"Student {i['name']} removed successfully")
                return print("student not found")
            
    def __str__(self):
        return "Inside str method"
        
        
obj1=College(2)
print(obj1)
obj1.AddStudent(1,'Ashu',23,98)
print(obj1.GetStudent(1))

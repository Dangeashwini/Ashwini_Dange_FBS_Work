from question1 import Emp
def addRecord():
    id=input("Enter your id:")
    name=input("Enter your name:")
    basic=int(input("Enter your salary:"))
    e1=Emp(id,name,basic)
    with open("core python/assignments/assignment22/record.txt",'a') as fp:
        fp.write(e1.showData())
    print("Record inserted successfully...")
def searchRecord():
    id=input("Enter the id to search:")
    with open("core python/assignments/assignment22/record.txt",'r') as fp:
        for line in fp:
            elist=line.strip().split(", ")
            if elist[0]==id:
               print(f"{elist[0]}, {elist[1]}, {elist[2]}\n")

def deleteRecord():
    id=input("Enter id to delete Record:")
    data=[]
    found=False
    with open("core python/assignments/assignment22/record.txt",'r') as fp:
        for line in fp:
            elist=line.strip().split(", ")
            if elist[0]==id:
                found=True
            else:
                data.append(line)
    with open("core python/assignments/assignment22/record.txt",'w') as fp:
        fp.writelines(data)
    if(found):
        print("Record deleted successfully")
    else:
        print("record not found")
        
                
                    
def editRecord():
    data=[]
    found=False
    id=input("Enter id to update record:")
    ch1=input("do you want to change name:y/n").lower()
    if ch1 in ['y','yes']:
        new_name=input("Enter your name:")
    else:
        new_name=None
    
    ch2=input("do you want to change salary:y/n").lower()
    if ch2 in ['y','yes']:
        
        new_sal=int(input("Enter new salary"))
    else:
        new_sal=None
    
    with open("core python/assignments/assignment22/record.txt",'r') as fp:
        for line in fp:
            elist=line.strip().split(", ")
            if elist[0]==id:
                found=True
                if new_name is not None:
                    elist[1]=new_name
                if new_sal is not None:
                    elist[2]=str(new_sal)
                updated=",".join(elist)+"\n"
                data.append(updated)
            else:
                data.append(line)
    with open("core python/assignments/assignment22/record.txt",'w') as fp:
        fp.writelines(data)
    if(found):
        print("Record updated successfully")
    else:
        print("no record found")      
        
def showAll():
    with open("core python/assignments/assignment22/record.txt",'r') as fp:
        for line in fp:
            print(line)
            
        
        

while(True):
    print('''Please select below option
          1. Add record
          2. Search record
          3. Delete record
          4. Edit record
          5. Display all record
          6. Exit
          ''')
    ch=input("Enter your choice:")
    if(ch=='1'):
        addRecord()
    elif(ch=='2'):
        searchRecord()
    elif(ch=='3'):
        deleteRecord()
    elif(ch=='4'):
        editRecord()
    elif(ch=='5'):
        showAll()
    elif(ch=='6'):
        print("thank you")
        break
    
    else:
        print("invalid choice")
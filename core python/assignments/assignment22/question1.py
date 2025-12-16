class Emp:
    def __init__(self,id,name,basic):
        self.id=id
        self.name=name
        self.basic=basic
        
    def showData(self):
        return f"{self.id}, {self.name}, {self.basic}"
    
if(__name__=='__main__'):
    e1=Emp(101,'ashwini',25000)
    print(e1.showData())
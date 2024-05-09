class student1(object):                 #1st parent class
    def __init__(self,rno):
        self.rno=rno
    def printdata1(self):
        print("The roll no. is =",self.rno)
        
class student2(object):                 #2nd parent class
    def __init__(self,age):
        self.age=age
    def printdata2(self):
        print("The age is =",self.age)
        
class derived(student1,student2):               #derives student1 and student2 class
    def __init__(self,name,rno,age):
        self.name=name
        student1.__init__(self,rno)
        student2.__init__(self,age)
    def printdata3(self):
        print("The name is =",self.name)
        
obj=derived("Lucy",236888,23)
obj.printdata1()
obj.printdata2()
obj.printdata3()

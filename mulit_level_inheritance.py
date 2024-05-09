class student1(object):                             #base class
    def __init__(self,rno):
        self.rno = rno
    def printdata1(self):
        print("The roll no. is  = ",self.rno)
        
class student2(student1):                           #base class for derived with derive student class
    def __init__(self,age,rno):
        student1.__init__(self,rno)
        self.age = age
    def printdata2(self):
        print("The age is  = ",self.age)
        
class derived(student2):                            #derives student2 class
    def __init__(self,name,rno,age):
        self.name = name
        student2.__init__(self,age,rno)
    def printdata3(self):
        print("The name is  = ",self.name)
        derived.printdata1(self)
        derived.printdata2(self)
        
obj = derived("Lucy",236888,21)
obj.printdata3()

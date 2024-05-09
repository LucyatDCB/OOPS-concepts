class student(object):                    #parent class
    def __init__(sel,rno):
        sel.rno=rno
    def printdata1(sel):
        print("The roll no. is =",sel.rno)

class derived(student):                     #derives the student class
    def __init__(sel,name,rno):
        sel.name=name
        student.__init__(sel,rno)
    def printdata2(sel):
        print("The name is =",sel.name)


obj=derived("Lucy",236888)
obj.printdata1()
obj.printdata2()

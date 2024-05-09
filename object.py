#This example demostrates the creation of objects for Student class

class Student:  
   def __init__(self, rollno, name):  
      self.rollno = rollno  
      self.name = name  
   def displayStudent(self):  
      print("rollno : ", self.rollno,  ", name: ", self.name)  


#object creation
emp1 = Student(121, "Lucy")  
emp2 = Student(122, "Batman")  

emp1.displayStudent()  
emp2.displayStudent() 

class Student:
   '����ѧ���Ļ���'
   stuCount = 1
 
   def __init__(self, name, stu_no, class_no, gender):
      self.name = name
      self.stu_no = stu_no
      self.class_no = class_no
      self.gender = gender
      Student.stuCount += 1
   
   def speakEnglish(self):
     print self.name, "can speak English."
 
   def canPrograme(self):
     print self.name, "can Programe."
      
   def canSwimming(self):
     print self.name, "can swimming."

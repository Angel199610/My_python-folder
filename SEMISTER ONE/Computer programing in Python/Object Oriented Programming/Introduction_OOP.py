#Class has attributes or properties e.g. (Bio data)
#objects are instances
class Student:
    def _init_(self, student_no, Name, email, contact, age, cohort):
        self.student_no = student_no
        self.Name = Name
        self.email = email
        self.contact = contact
        self.age = age
        self.cohort = cohort

#Function to call for the name and student number
    def __str__(self):
        return f"{self.Name}, {self.student_no}"
    
    def name_email_cohort(self):
        return f"{self.Name}, {self.email}, {self.cohort}"

#To creat an object make sure you are out of the indention of self column
#CREATING GOBJECTS WHICH ARE INSTANCES
student1=Student("2023/DSCE/00106/SS", "Kwagala Angel", "kwagalaangel27@gmail.com", "0785220954", "27", "Cohort III")
print(student1.name_email_cohort())
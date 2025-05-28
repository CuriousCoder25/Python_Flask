#5/27
class student:
    def __init__ (self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def display_student_details(self):
        print(f"Name: {self.name} Roll.no: {self.roll_no} Average Marks: {self.average}")
    
    def average(self):
        return sum(self.marks)/len(self.marks)
        
gaurav=student("Gaurav",7,[99,99,89,98,78])
gaurav.display_student_details()
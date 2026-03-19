class Student:
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks

        
    def get_grade(self):
        if (self.marks >= 90):
            return ("You got A+ Grade.")
        elif (self.marks >= 70):
            return ("You got B+ Grade.")
        else:
            return "You got C Grade."


s1 = Student("Talha", 90)
print (s1.get_grade())
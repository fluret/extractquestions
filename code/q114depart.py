class HighSchoolStudent(Student):  # Add the parent class inside the parenthesis
    def __init__(self, name, age, grade, specialization):
        super().__init__(name, age, grade)
        self.specialization = specialization

    def study(self, hours):
        return f"{self.name} is a high school student specializing in {self.specialization} and is studying for {hours} hours for exams."


# Creating an instance of HighSchoolStudent
high_school_student = HighSchoolStudent("John", 16, 85, "Science")
print(high_school_student.introduce())  # We can call this method thanks to inheritance
print(
    high_school_student.study(4)
)  # This method has been slightly modified and now it returns a different string

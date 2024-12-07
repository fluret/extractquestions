### code départ
class HighSchoolStudent(Student):  # Add the parent class inside the parenthesis
    def __init__(self, name, age, grade, specialization):
        super().__init__(name, age, grade)
        self.specialization = specialization

    def study(self, hours):
        return f"{self.name} is a high school student specializing in {self.specialization} and is studying for {hours} hours for exams."

# Creating an instance of HighSchoolStudent
high_school_student = HighSchoolStudent("John", 16, 85, "Science")
print(high_school_student.introduce())  # We can call this method thanks to inheritance 
print(high_school_student.study(4))  # This method has been slightly modified and now it returns a different string
### correction
### DON'T modify this code ###

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self):
        return f"Hello! I am {self.name}, I am {self.age} years old, and my current grade is {self.grade}."

    def study(self, hours):
        return f"{self.name} is studying for {hours} hours."
        
### DON'T modify the code above ###
        
### ↓ Your code here ↓ ###

class CollegeStudent(Student):
    def __init__(self, name, age, grade, major):
        super().__init__(name, age, grade)
        self.major = major

    def introduce(self):
        return f"Hi there! I'm {self.name}, a college student majoring in {self.major}."

    def attend_lecture(self):
        return f"{self.name} is attending a lecture for {self.major} students."


college_student = CollegeStudent("Alice", 20, 90, "Computer Science")
print(college_student.introduce())
print(college_student.study(3))
print(college_student.attend_lecture())
### test.py
import pytest
from app import CollegeStudent

@pytest.mark.it("The CollegeStudent class should exist")
def test_college_student_class_exists():
    try:
        assert CollegeStudent
    except AttributeError:
        raise AttributeError("The class 'CollegeStudent' should exist in app.py")

@pytest.mark.it("The CollegeStudent class includes the 'name' attribute")
def test_college_student_has_name_attribute():
    college_student = CollegeStudent("John", 21, 75, "Computer Science")
    assert hasattr(college_student, "name")

@pytest.mark.it("The CollegeStudent class includes the 'age' attribute")
def test_college_student_has_age_attribute():
    college_student = CollegeStudent("John", 21, 75, "Computer Science")
    assert hasattr(college_student, "age")

@pytest.mark.it("The CollegeStudent class includes the 'grade' attribute")
def test_college_student_has_grade_attribute():
    college_student = CollegeStudent("John", 21, 75, "Computer Science")
    assert hasattr(college_student, "grade")

@pytest.mark.it("The CollegeStudent class includes the 'major' attribute")
def test_college_student_has_major_attribute():
    college_student = CollegeStudent("John", 21, 75, "Computer Science")
    assert hasattr(college_student, "major")

@pytest.mark.it("The CollegeStudent class includes the 'introduce' method")
def test_college_student_has_introduce_method():
    college_student = CollegeStudent("Alice", 22, 90, "Computer Science")
    assert hasattr(college_student, "introduce")

@pytest.mark.it("The CollegeStudent class includes the 'study' method")
def test_college_student_has_study_method():
    college_student = CollegeStudent("John", 21, 75, "Computer Science")
    assert hasattr(college_student, "study")    

@pytest.mark.it("The CollegeStudent class includes the 'attend_lecture' method")
def test_college_student_has_attend_lecture_method():
    college_student = CollegeStudent("John", 21, 75, "Computer Science")
    assert hasattr(college_student, "attend_lecture")

@pytest.mark.it("The introduce method should return the expected string. Testing with different values")
def test_college_student_introduce_method_returns_expected_string():
    student1 = CollegeStudent("Alice", 22, 90, "Computer Science")
    student2 = CollegeStudent("Bob", 19, 85, "Mathematics")
    assert student1.introduce() == "Hi there! I'm Alice, a college student majoring in Computer Science."
    assert student2.introduce() == "Hi there! I'm Bob, a college student majoring in Mathematics."

@pytest.mark.it("The study method should return the expected string. Testing with different values")
def test_college_student_study_method_returns_expected_string():
    student1 = CollegeStudent("Eve", 20, 78, "Physics")
    student2 = CollegeStudent("Charlie", 23, 88, "Chemistry")
    assert student1.study(3) == "Eve is studying for 3 hours."
    assert student2.study(2) == "Charlie is studying for 2 hours."

@pytest.mark.it("The attend_lecture method should return the expected string. Testing with different values")
def test_college_student_attend_lecture_method_returns_expected_string():
    student1 = CollegeStudent("Eve", 20, 78, "Physics")
    student2 = CollegeStudent("Charlie", 23, 88, "Chemistry")
    assert student1.attend_lecture() == "Eve is attending a lecture for Physics students."
    assert student2.attend_lecture() == "Charlie is attending a lecture for Chemistry students."
def get_letter_grade(grade):
    if grade >= 100:
        print("Please enter a grade between 0-100")
    elif grade >= 90:
        print(f"{grade} is an A")
    elif grade >= 80:
        print(f"{grade} is a B")
    elif grade >= 70:
        print(f"{grade} is a C")
    elif grade >= 60:
        print(f"{grade} is a D")
    elif grade <= 59 and grade >= 0:
        print(f"{grade} is an F")
    else:
        print("No negative numbers")


get_letter_grade(95)
get_letter_grade(85)
get_letter_grade(75)
get_letter_grade(65)
get_letter_grade(55)
get_letter_grade(0)
get_letter_grade(105)
get_letter_grade(-5)

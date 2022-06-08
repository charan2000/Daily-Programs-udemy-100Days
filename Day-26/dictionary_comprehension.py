import random

students = ["Ariel", "Brian", "Stewie", "Peter", "Zill"]
new_dict = {student: random.randint(1, 100) for student in students}

passed_students = {student: marks for (student, marks) in new_dict.items() if marks >= 55}
print(passed_students)
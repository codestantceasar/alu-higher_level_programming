#!/usr/bin/python3
Student = __import__('9-student').Student

students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

for student in students:
    j_student = student.to_json()
    print(type(j_student))  # This will print <class 'dict'>
    print(j_student['first_name'])  # Prints the first_name attribute
    print(type(j_student['first_name']))  # Prints <class 'str'>
    print(j_student['age'])  # Prints the age attribute
    print(type(j_student['age']))  # Prints <class 'int'>

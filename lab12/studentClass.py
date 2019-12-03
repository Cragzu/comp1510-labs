# Clint F & Chloe G

"""Module defining a student class and performing some basic example methods on it."""
import math

STUDENT_NUMBER_DIGITS = 8


class Student:

    students = 0

    def __init__(self, first_name: str, surname: str, passed_classes: dict, middle_name: str = ''):
        self.__first_name = first_name.title()
        self.__surname = surname.title()

        self.__student_number = 'A'
        for i in range(STUDENT_NUMBER_DIGITS - len(str(Student.students))):
            self.__student_number += '0'

        self.__student_number += str(Student.students)
        Student.students += 1

        self.__passed_classes = passed_classes
        self.__middle_name = middle_name.title()

    def get_gpa(self) -> float:
        gpa = 0
        for v in self.__passed_classes.values():
            gpa += v

        gpa /= len(self.__passed_classes)
        return math.trunc(gpa)  # truncated average of all grades

    def get_student_info(self) -> str:
        if self.__middle_name:  # check for middle name to prevent extra spaces
            name_line = 'Name: ' + self.__first_name + ' ' + self.__middle_name + ' ' + self.__surname + '\n'
        else:
            name_line = 'Name: ' + self.__first_name + ' ' + self.__surname + '\n'

        student_number_line = 'Student number: ' + self.__student_number + '\n'
        classes_line = 'Number of courses: ' + str(len(self.__passed_classes)) + '\n'
        gpa_line = 'GPA: ' + str(self.get_gpa())

        return name_line + student_number_line + classes_line + gpa_line  # formatted string output

    def change_surname(self, new_surname: str):
        self.__surname = new_surname

    def add_course(self, new_course: str, new_grade: float):
        self.__passed_classes[new_course] = new_grade


def main():
    nicole = Student('Nicole', 'Brooks', {'COMP 1510': 95.0, 'COMP 1113': 87.0, 'COMP 1536': 94.0},
                     'Paige')
    cornelius = Student('Cornelius', 'Smith', {'COMM 1116': 45.0, 'COMP 1930': 65.0, 'COMP 1712': 75.0})

    harold = Student('Harold', 'Finch', {'COMP 1510': 37.0, 'COMP 1712': 40.0, 'COMM 1116': 0.0})

    print(nicole.get_student_info())
    print(cornelius.get_student_info())
    print(harold.get_student_info())

    nicole.change_surname('Wang')
    print(nicole.get_student_info())


if __name__ == '__main__':
    main()




class Person:


    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student(Person):

    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def enroll_course(self, course_name):
        print(f"{self.name} (Student ID: {self.student_id}) has enrolled in '{course_name}'.")


class Lecturer(Person):

    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def teach_course(self, course_name):
        print(f"{self.name} (Employee ID: {self.employee_id}) is teaching '{course_name}'.")

    def display_info(self):

        print("--- Lecturer Info ---")
        super().display_info()          # prints name and age
        print(f"Employee ID: {self.employee_id}")


if __name__ == "__main__":

    student1 = Student("COBBINAH ALBERT", 17, "FOE.41.006.071,25")
    student1.display_info()
    student1.enroll_course("Introduction to Object Oriented Programming")


    lecturer1 = Lecturer("Dr. COBBINAH MATTHEW", 45, "UMaT/EMP/2010/045")
    lecturer1.display_info()
    lecturer1.teach_course("OOP")
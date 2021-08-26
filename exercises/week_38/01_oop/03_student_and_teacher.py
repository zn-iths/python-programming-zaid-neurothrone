from shared.week_38_oop import Person


class Student(Person):
    @staticmethod
    def study() -> None:
        print("study...study...study...more study")


class Teacher(Person):
    @staticmethod
    def teach() -> None:
        print("teach...teach...teach...more teaching")


student = Student("Zaid", 30, "zaid@example.com")
teacher = Teacher("Danny", 45, "danny@example.com")

student.study()
student.say_hello()
teacher.teach()
teacher.say_hello()

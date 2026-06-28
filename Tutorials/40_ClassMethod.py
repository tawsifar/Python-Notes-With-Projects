class Student:

    # class variables — shared across ALL instances, not tied to any single object
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name    # instance variable — this student's own name
        self.gpa = gpa      # instance variable — this student's own gpa
        Student.count += 1          # every time a new student is created, class counter goes up
        Student.total_gpa += gpa    # running total of all gpas across all students

    # instance method — needs self, works on this specific student's data
    def get_info(self):
        return f"{self.name} : {self.gpa}"

    # class method — takes cls instead of self, cls points to the class itself
    # used when the operation involves class-level data, not any single object
    @classmethod
    def get_count(cls):
        return f"Total students: {cls.count}"  # cls.count = Student.count, same thing

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return "No students yet"
        return f"Average GPA: {cls.total_gpa / cls.count:.2f}"  # :.2f = 2 decimal places


# each object creation triggers __init__, which updates count and total_gpa
student1 = Student("Spongebob", 3.2)   # count=1, total_gpa=3.2
student2 = Student("Patrick", 2.0)     # count=2, total_gpa=5.2
student3 = Student("Sandy", 4.0)       # count=3, total_gpa=9.2

# instance method — called on a specific object
print(student1.get_info())   # Spongebob : 3.2
print(student2.get_info())   # Patrick : 2.0
print(student3.get_info())   # Sandy : 4.0

# class method — called on the class itself, no object needed
print(Student.get_count())        # Total students: 3
print(Student.get_average_gpa())  # Average GPA: 3.07

# class method can also be called on an object, result is the same
# because cls always points to the class, not the object
print(student1.get_count())       # Total students: 3


# edge case — what if no students exist yet?
class Course:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Course.count += 1
        Course.total_gpa += gpa

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return "No students enrolled yet"
        return f"Average GPA: {cls.total_gpa / cls.count:.2f}"

print(Course.get_average_gpa())   # No students enrolled yet — safe, no division by zero
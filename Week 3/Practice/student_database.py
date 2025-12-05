students = {}

def add_student(name, age):
    students[name] = age

def get_student(name):
    return students.get(name, "Student not found")

def display_all():
    for name, age in students.items():
        print(name, "-", age)

# Test
add_student("Amit", 20)
add_student("Priya", 22)

print(get_student("Amit"))
display_all()

def calculate_grade(marks):
    if marks >= 90:
        return "A+", "Excellent"
    elif marks >= 80:
        return "A", "Very Good"
    elif marks >= 70:
        return "B", "Good"
    elif marks >= 60:
        return "C", "Average"
    elif marks >= 50:
        return "D", "Needs Improvement"
    else:
        return "F", "Fail"

students = []
n = int(input("Enter number of students: "))

for i in range(n):
    name = input(f"\nEnter name of student {i+1}: ")
    marks = float(input("Enter marks (out of 100): "))
    grade, comment = calculate_grade(marks)
    students.append({"Name": name, "Marks": marks, "Grade": grade, "Comment": comment})

print("\n📋 Student Grade Report:")
print("----------------------------------------------------")
for s in students:
    print(f"{s['Name']:15} | Marks: {s['Marks']:5} | Grade: {s['Grade']:2} | {s['Comment']}")
print("----------------------------------------------------")

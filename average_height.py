# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
height_total = 0
students_number = 0
for height in student_heights:
    height_total += height
    students_number += 1

print(f"total height = {height_total}")

print(f"number of students = {students_number}")

print(f"average height = {round(height_total / students_number)}")

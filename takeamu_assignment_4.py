student_name = "Tehcubelleh Keamu"
current_gpa = 3.5
study_hours = 20
social_points = 40
stress_level = 87

print(f"Hello {student_name}")
print("")
print("Choose your course load:")
print("A) Light (12 credits)")
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")

choice = input("Your choice: ")

if choice == "A":
    if current_gpa >= 3.5:
        stress_level -= 10
        study_hours -= 5
        current_gpa += 0.03
    else:
        stress_level += 2
        study_hours += 1
        current_gpa += 0.08
elif choice == "B":
    if current_gpa >= 3.5:
        stress_level -= 5
        study_hours -= 2
        current_gpa += 0.05
    else:
        stress_level += 3
        study_hours += 4
        current_gpa += 0.06
elif choice == "C":
    if current_gpa >= 3.5:
        stress_level += 3
        study_hours += 2
        current_gpa += 0.07
    else:
        stress_level += 6
        study_hours += 5
        current_gpa += 0.1
else:
    print("invalid input")

print(f"GPA: {round(current_gpa, 2)}")
print(f"Study Hours: {study_hours}")
print(f"Stress Level: {stress_level}")
print(f"Social Points: {social_points}")
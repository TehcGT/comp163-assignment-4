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

study_options = ["Programming", "Math", "English", "History"]
print("Choose a class to study: ")
print(study_options)
choice = input("Choice selected: ")

if choice in study_options:
    if choice == "Programming":
        current_gpa += 0.2
        social_points -= 5
        print("Kind of hard subject, you get less freedom and more study time")

    elif choice == "Math":
        current_gpa += 0.3
        social_points -= 2
        print("Math? Interesting choice")

    elif choice == "English" and current_gpa >= 3.0:
        social_points += 10
        current_gpa += 0.05
        print("Balenced as all things should be...")

    elif choice == "History" or (choice == "English" and current_gpa < 3.0):
        current_gpa += 0.1
        social_points += 3
        print("Nice one! at this rate you'll make millions.")

elif choice not in study_options:
    print("Invalid choice. Please select from the list.")

print(f"\nUpdated GPA: {round(current_gpa, 2)}")
print(f"Updated Social Points: {social_points}")
student_name = input("Enter your name: ")
current_gpa = float(input("Enter your current GPA 1.0-4.0: "))
study_hours = int(input("Enter your study hours: "))
social_points = int(input("Enter your social points: "))
stress_level = int(input("Enter your stress level 1-100: "))

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

print(f"Updated GPA: {round(current_gpa, 2)}")
print(f"Updated Social Points: {social_points}")
print("")
ready_status = "READY"
ending = ready_status
print("OKAY AND...Drumroll please")
print("")
if ready_status is not ending:
    print("You can't read or spell...")

elif ready_status is ending:
    if current_gpa >= 3.7:
        print("ASSESSMENT: ACADEMIC EXCELLENCE!")
        if stress_level < 75 and social_points >= 40:
            print("ENDING 1: Academic warrior!")
            print("You achieved a high GPA and maintained a healthy social life with low stress. You mastered the college challenge!")
    elif stress_level >= 75 and social_points < 40:
        print("ENDING 2: I did it...*Faints*")
        print("You achieved a high GPA, but your high stress and low social points suggest severe burnout. Take a break—your mental health is failing!")
    else:
        print("ENDING 3: I am just like that, what's next")
        print("You achieved a high GPA with a generally balanced outcome. Ready for the next challenge!")

elif current_gpa >= 3.0 and current_gpa < 3.7:
    print("ASSESSMENT: SOLID PERFORMANCE.")
    if study_hours < 25 and social_points > 50:
        print("ENDING 4: Im done with work guys, lets hang!")
        print("Your GPA is average, but you have very high social capital. You focused on networking and relationships over textbooks.")
    else:
        print("ENDING 5: One more thing... andddd done!")
        print("You passed the semester comfortably and maintained a manageable workload. Good, steady progress.")

elif current_gpa <= 2.9:
    print("ASSESSMENT: ACADEMIC STRUGGLE.")
    if stress_level >= 90 and current_gpa <= 2.5:
        print("ENDING 6: Dropping out never looked so nice *maniac laughter*")
        print("Your low GPA combined with extreme stress suggests a critical semester failure. Intervention is required.")
    else:
        print("ENDING 7: Uh oh, I must study harder")
        print("Your GPA is low. You need to reassess your priorities and increase your study hours next semester.")

print("FINAL RESULTS")
print(f"GPA: {round(current_gpa, 2)}")
print(f"Study Hours: {study_hours}")
print(f"Stress Level: {stress_level}")
print(f"Social Points: {social_points}")
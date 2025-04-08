written = float(input("Enter the marks scored in Written test: "))
lab = float(input("Enter the marks scored in Lab exams: "))
assignment = float(input("Enter the marks scored in Assignments: "))
grade = (written * 70) / 100 + (lab * 20) / 100 + (assignment * 10) / 100
print("Grade of the student is",grade)

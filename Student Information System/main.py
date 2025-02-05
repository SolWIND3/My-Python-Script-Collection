import json
class Student:
    def __init__(self, student_name, id_num, contact, email):
        self.student_name = student_name
        self.id_num = id_num
        self.contact = contact
        self.email = email
    def __str__(self):
        return f"STUDENT NAME: {self.student_name}\nID NUMBER: {self.id_num}\nCONTACT NUMBER: {self.contact}\nEMAIL: {self.email}"
    def to_json(self):
        return {
            "student_name": self.student_name,
            "id_num": self.id_num,
            "contact": self.contact,
            "email": self.email,
        }
def student_search(students, student_name):
    for student in students:
        if student.student_name.lower() == student_name.lower():
            return student
    return None
students = []
def add_student():
    student_name = input("Enter the student's FULL name: ")
    id_num = input("Enter the student's ID number: ")
    contact = input("Enter the student's contact number: ")
    email = input("Enter the student's email: ")
    new_student = Student(student_name, id_num, contact, email)
    students.append(new_student)
    print(f"[Student {student_name} has been added to the database.]")
def save_students():
    with open("students.json", "a") as f:
        json.dump([student.to_json() for student in students], f)
while True:
    print("╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("  Welcome to this simple student information system for [Section] Students! What would you like to do?  ")
    print("╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("|                                   [SECTION] STUDENT INFORMATION SYS                                  |")
    print("╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("|                                   [1].I Want to Search for a Student                                 |")
    print("|                                   [2].Add a New Student                                              |")
    print("|                                   [3].Save Student information                                       |")
    print("|                                   [4].View All Students in SaveFile                                  |")
    print("|                                   [5].Quit                                                           |")
    print("╚══════════════════════════════════════════════════════════════════════════════════════════════════════╝")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("╔═══════════════════════════════════════════════════════════════════════╗")
        name = input("   Enter the student's FULL name: ")
        print("   ")
        student = student_search(students, name)
        if student is not None:
            print(student)
        else:
            print("[No Such Student Exists.]")
    elif choice == "2":
        add_student()
    elif choice == "3":
        save_students()
        print("[Complete]")
    elif choice == "5":
        print("[Quitting...]")
        break
    elif choice == "4":
      print("[LIST OF ALL STUDENTS CURRENTLY STORED IN STUDENTS.JSON(SAVEFILE)]")
      with open("students.json") as json_file:
        students = json.load(json_file)
        print(json.dumps(students, indent=1))
        print(" ")
        print("[REACHED END OF SAVEFILE]")
    else:
        print("[Invalid!]")
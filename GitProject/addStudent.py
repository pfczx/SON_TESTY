from exportStudents import ExportStudents
import os


class ModifyStudents:
    # method to add student to list and export it to csv and txt files, files are deleted after operation and new list overwrite file
    @staticmethod
    def add_student_and_export(path, path2, students):
        name = input("Enter student's name: ")
        surname = input("Enter student's surname: ")
        student_id = input("Enter student's ID: ")
        students.append({"Name": name, "Surname": surname, "ID": student_id})
        ExportStudents.csv(path, students)
        ExportStudents.txt(path2, students)

    # method to add student to file, if file doesn't exist, it will create it
    @staticmethod
    def add_student_by_overwriting(path, path2):
        student = [input("Enter student's name: "), input("Enter student's surname: "), input("Enter student's ID: ")]
        if os.path.exists(path) and os.path.exists(path2):
            file = open(path, "a")
            file2 = open(path2, "a")
            file.write("\n" + ";".join(student))
            file2.write("\n" + student[0] + " " + student[1] + " - " + student[2])
        else:
            file = open(path, "a")
            file2 = open(path2, "a")
            file.write(";".join(student))
            file2.write(student[0] + " " + student[1] + " - " + student[2])

    @staticmethod
    def modify_student(path, path2, students):
        student_id = input("Enter student's ID to modify: ")
        for student in students:
            if student["ID"] == student_id:
                name = input("Enter new student's name: ")
                surname = input("Enter new student's surname: ")
                student["Name"] = name
                student["Surname"] = surname
                ExportStudents.csv(path, students)
                ExportStudents.txt(path2, students)
                return
        print("Student not found.")








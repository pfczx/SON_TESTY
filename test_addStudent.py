import pytest


class MockModifyStudents:
    @staticmethod
    def add_student(students,test_name,test_surname,test_id):
        #name = input("Enter student's name: ")
        name = test_name
        #surname = input("Enter student's surname: ")
        surname = test_surname
        #student_id = input("Enter student's ID: ")
        student_id = test_id
        students.append({"Name": name, "Surname": surname, "ID": student_id})

    @staticmethod
    def modify_student(students,test_id,test_name,test_surname):
        #student_id = input("Enter student's ID to modify: ")
        student_id = test_id
        for student in students:
            if student["ID"] == student_id:
                #name = input("Enter new student's name: ")
                name = test_name
                #surname = input("Enter new student's surname: ")
                surname=test_surname
                student["Name"] = name
                student["Surname"] = surname
                return
        print("Student not found.")


class Testing:
    @staticmethod
    def test_add_student():
        #given
        listOfStudents=[]
        want=[{"Name": "Tomek", "Surname": "Ananas", "ID": "777ABC"}]

        #when
        MockModifyStudents.add_student(listOfStudents,"Tomek","Ananas","777ABC")

        #then
        assert want==listOfStudents
    @staticmethod
    def test_modify_student():
        #given
        listOfStudents = [{ "Name": "Tomek", "Surname": "Ananas", "ID": "777ABC"}]
        want = [{"Name": "Maciek", "Surname": "Poziomka", "ID": "777ABC"}]
        #when
        MockModifyStudents.modify_student(listOfStudents,"777ABC","Maciek","Poziomka")
        #then
        assert want==listOfStudents
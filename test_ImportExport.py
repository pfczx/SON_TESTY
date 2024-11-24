import pytest
import os




class ImportStudents:
    @staticmethod
    def csv(path, student_details_structure):
        students = []

        file = open(path, "r")

        for line in file:
            line = line.rstrip()

            student_details_dict = {}

            student_details = line.split(";")

            for i in range(len(student_details_structure)):
                student_details_dict[student_details_structure[i]] = student_details[i]

            students.append(student_details_dict)

        return students

class ExportStudents:
    @staticmethod
    def csv(path, list):
        file = open(path, "w")

        lines = []

        for i in range(0, len(list)):
            student_details = list[i]
            line = []

            for student_detail_key in student_details:
                line.append(student_details[student_detail_key])

            line = ";".join(line)

            if i < len(list) - 1:
                line += "\n"

            lines.append(line)

        file.writelines(lines)

class Testing:

    @staticmethod
    def test_import_students():
        #given
        # Given
        path = "test_students_import.csv"
        student_details_structure = ["Name", "Surname", "ID"]
        file_content = """Johan;Andre-Forfang;777\nGeorge;Droid;432AHFDV"""
        with open(path, "w") as file:
            file.write(file_content)
        want = [
            {"Name": "Johan", "Surname": "Andre-Forfang", "ID": "777"},{"Name": "George", "Surname": "Droid", "ID": "432AHFDV"}]
        #when
        got = ImportStudents.csv(path, student_details_structure)
        #then
        assert want == got
        os.remove(path)

    @staticmethod
    def test_export_students():
        # given
        path="test_students_export.csv"
        students = [
            {"Name": "Noriaki", "Surname": "Kasai","ID": "777"},
            {"Name": "George", "Surname": "Fent","ID": "777"}
        ]
        with open(path, "w") as file:
            pass
        want = """Noriaki;Kasai;777\nGeorge;Fent;777"""
        # when
        ExportStudents.csv(path, students)
        with open(path, "r") as file:
            got = file.read().strip()
        #then
        assert got ==want
        os.remove(path)


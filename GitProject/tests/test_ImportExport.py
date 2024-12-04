import os
from GitProject.mainFuncitions.exportStudents import ExportStudents
from GitProject.mainFuncitions.importStudents import ImportStudents


class Testing:

    @staticmethod
    def test_import_students():
        #given
        base_dir = os.path.dirname(os.path.abspath(__file__))
        pathtxt = os.path.join(base_dir, '../testLists/studentTestList.txt')
        pathcsv = os.path.join(base_dir, '../testLists/studentTestList.csv')
        student_details_structure = ["Name", "Surname", "ID"]
        txtContent = "Johan Andre-Forfang - 777\nGeorge Droid - 432AHFDV"
        csvContent = """Johan;Andre-Forfang;777\nGeorge;Droid;432AHFDV"""
        with open(pathcsv, "w") as file:
            file.write(csvContent)
        with open(pathtxt, "w") as file:
            file.write(txtContent)
        expectedListContent = [{"Name": "Johan", "Surname": "Andre-Forfang", "ID": "777"},{"Name": "George", "Surname": "Droid", "ID": "432AHFDV"}]

        #when
        importedCsv = ImportStudents.csv(pathcsv, student_details_structure)
        importedTxt = ImportStudents.txt(pathtxt, student_details_structure)

        #then
        assert importedCsv == expectedListContent
        assert importedTxt == expectedListContent
        if os.path.exists(pathtxt):
            os.remove(pathtxt)
        if os.path.exists(pathcsv):
            os.remove(pathcsv)

    @staticmethod
    def test_export_students():
        # given
        base_dir = os.path.dirname(os.path.abspath(__file__))
        pathtxt = os.path.join(base_dir, '../testLists/studentTestList.txt')
        pathcsv = os.path.join(base_dir, '../testLists/studentTestList.csv')
        expectedCsvContent = """Noriaki;Kasai;777\nGeorge;Fent;777"""
        expectedTxtContent= "Noriaki Kasai - 777\nGeorge Fent - 777"
        students = [
            {"Name": "Noriaki", "Surname": "Kasai","ID": "777"},
            {"Name": "George", "Surname": "Fent","ID": "777"}
        ]
        with open(pathcsv, "w") as file:
            pass
        with open(pathtxt, "w") as file:
            pass

        # when
        ExportStudents.csv(pathcsv, students)
        ExportStudents.txt(pathtxt, students)
        with open(pathcsv, "r") as file:
            csvFileContent = file.read().strip()
        with open(pathtxt, "r") as file:
            txtFileContent = file.read().strip()
        #then
        assert csvFileContent == expectedCsvContent
        assert txtFileContent == expectedTxtContent
        if os.path.exists(pathtxt):
            os.remove(pathtxt)
        if os.path.exists(pathcsv):
            os.remove(pathcsv)


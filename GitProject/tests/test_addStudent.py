from GitProject.mainFuncitions.addStudent import ModifyStudents
from unittest.mock import patch
import os


class Testing:
    @staticmethod
    def test_add_student():
        #given
        base_dir = os.path.dirname(os.path.abspath(__file__))
        pathtxt = os.path.join(base_dir, '../testLists/studentTestList.txt')
        pathcsv = os.path.join(base_dir, '../testLists/studentTestList.csv')
        listOfStudents=[]
        expectedListContent=[{"Name": "Tomek", "Surname": "Ananas", "ID": "777ABC"}]
        expectedTxtContent="Tomek Ananas - 777ABC"
        expectedCsvContent="Tomek;Ananas;777ABC"
        with open(pathtxt, 'w') as f:
            pass
        with open(pathcsv, 'w') as f:
            pass

        #when
        with patch('builtins.input', side_effect=["Tomek", "Ananas","777ABC"]):
            ModifyStudents.add_student_and_export(pathcsv,pathtxt,listOfStudents)
        with open(pathtxt, 'r') as f:
            txtContent = f.read().strip()
        with open(pathcsv, 'r') as f:
            csvContent = f.read().strip()

        #then
        assert expectedListContent==listOfStudents
        assert expectedCsvContent==csvContent
        assert expectedTxtContent==txtContent
        if os.path.exists(pathtxt):
            os.remove(pathtxt)
        if os.path.exists(pathcsv):
            os.remove(pathcsv)
    @staticmethod
    def test_modify_student():
        #given
        base_dir = os.path.dirname(os.path.abspath(__file__))
        pathtxt = os.path.join(base_dir, '../testLists/studentTestList.txt')
        pathcsv = os.path.join(base_dir, '../testLists/studentTestList.csv')
        listOfStudents = [{ "Name": "Tomek", "Surname": "Ananas", "ID": "777ABC"}]
        expectedListContent = [{"Name": "Maciek", "Surname": "Poziomka", "ID": "777ABC"}]
        expectedTxtContent = "Maciek Poziomka - 777ABC"
        expectedCsvContent = "Maciek;Poziomka;777ABC"
        with open(pathtxt, 'w') as f:
            pass
        with open(pathcsv, 'w') as f:
            pass


        #when
        with patch('builtins.input', side_effect=["777ABC", "Maciek","Poziomka"]):
            ModifyStudents.modify_student(pathcsv,pathtxt,listOfStudents)
        with open(pathtxt, 'r') as f:
            txtContent = f.read().strip()
        with open(pathcsv, 'r') as f:
            csvContent = f.read().strip()
        #then
        assert expectedListContent==listOfStudents
        assert expectedCsvContent==csvContent
        assert expectedTxtContent==txtContent
        if os.path.exists(pathtxt):
            os.remove(pathtxt)
        if os.path.exists(pathcsv):
            os.remove(pathcsv)
from GitProject.mainFuncitions.attendance import Attendance
from unittest.mock import patch

class Testing:
    @staticmethod
    def test_check_attendance_for_all():
        #given
        attendance = Attendance()
        date = "2000-09-20"
        students = [
            {"Name": "Noriaki", "Surname": "Kasai"},
            {"Name": "George", "Surname": "Fent"}
        ]
        want ={"2000-09-20":{"Noriaki Kasai":True,"George Fent":False}}
        #when
        with patch('builtins.input', side_effect=["1","0"]):
            attendance.check_attendance_for_all(date, students)
        got = attendance.presence
        #then
        assert want == got

    @staticmethod
    def test_clear_attendance():
        # given
        attendance = Attendance()
        date = "2000-09-20"
        attendance.presence = {date: {"Noriaki Kasai": True, "George Fent": True}}
        want = {}
        # when
        attendance.clear_attendance(date)
        got = attendance.presence
        #then
        assert got == want
    @staticmethod
    def test_modify_attendance():
        #given
        attendance = Attendance()
        date = "2000-09-20"
        attendance.presence = {date: {"Noriaki Kasai": True, "George Fent": True}}
        studentName1 = "Noriaki Kasai"
        studentName2 = "George Fent"
        want = {date: {"Noriaki Kasai": True, "George Fent": False}}
        #when
        with patch('builtins.input', side_effect=["1"]):
            attendance.modify_attendance(date, studentName1)
        with patch('builtins.input', side_effect=["0"]):
            attendance.modify_attendance(date, studentName2)
        #then
        assert want == attendance.presence
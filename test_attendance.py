import pytest
import os

class Attendance:
    def __init__(self):
        self.presence = {}

    # Iterating through the list of students to check attendance
    def check_attendance_for_all(self, date, students,test_inputPresent):
        if date not in self.presence:
            self.presence[date] = {}

        for student in students:
            student_name = f"{student['Name']} {student['Surname']}"
            #present = input(f"Is {student_name} present? (1/0): ") == "1"
            present=test_inputPresent
            self.presence[date][student_name] = present
            print(f"Attendance for student {student_name} on {date} has been updated to {'present' if present else 'absent'}.\n")



    # Clearing attendance data
    def clear_attendance(self, date):
        if date in self.presence:
            del self.presence[date]
            print(f"Attendance data for {date} has been removed.")
        else:
            print(f"No attendance data for {date}.")


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
        want ={"2000-09-20":{"Noriaki Kasai":True,"George Fent":True}}
        #when
        attendance.check_attendance_for_all(date, students,True)
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

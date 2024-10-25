class ImportStudents:
    student_details_structure = ["Name", "Surname", "ID"]

    @staticmethod
    def csv(path):

        student_details_structure = ImportStudents.student_details_structure

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

    @staticmethod
    def txt(path):

        student_details_structure = ImportStudents.student_details_structure

        students = []

        file = open(path, "r")

        for line in file:
            line = line.rstrip()

            student_details_dict = {}

            student_details = [j for i in line.split(" - ") for j in i.split(" ")]

            for i in range(len(student_details_structure)):
                student_details_dict[student_details_structure[i]] = student_details[i]

            students.append(student_details_dict)

        return students
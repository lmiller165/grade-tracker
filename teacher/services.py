from main.models import CustomUser, Course, Grade, Gpa
from main import constants as c
from student.models import Student
import csv


class CSV:
    """
    CSV to handle csv updloads from teachers and admin.
    It registers students and updates their grades
    """
    def __init__(self, my_csv):
        with open(f'./media/csv/{my_csv}', mode='r') as csv_file:
            self.csv = csv.reader(csv_file)
            self.csv = list(self.csv)
            # save column names
            self.columns = list(self.csv[2])
            # start with students
            self.csv = self.csv[3:]


    def register_students(self):
        """
        Find any students that are not registered as users
        and create a new user for them with student profile.
        """
        # TODO: Fix how emails are added if we are able to export emails
        counter = 0
        for entry in self.csv:
            counter += 1
            if not Student.objects.filter(calstudentID=entry[3]).exists():
                name = entry[2]
                name = name.split(', ')
                last_name = name[0]
                first_name = name[1]

                user = CustomUser.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    email=f'student{counter}@gmail.com', 
                    password=c.DEFAULT_PASSWORD, 
                    is_student=True)

                student_profile = Student.objects.create(
                    user=user,
                    grade_level=entry[1],
                    calstudentID=entry[3],
                    race=entry[5].lower(),
                    is_iep=bool(entry[7] == 'Students with an IEP'),
                    ell_status=entry[8],
                    on_reduced_lunch=bool(entry[9] != 'Ineligible')
                    )

                student_profile.save()
        return "Success"


    def register_courses(self):
        """
        Will look for any unregistered coursed and create a course if not found.
        """
        for subject in self.columns[10:]:
            # TODO: ask for term start and end date when registering course
            if not Course.objects.filter(title=subject).exists():
                course = Course.objects.create(
                    title=subject,
                    term='S1',
                    credit_hours=c.DEFAULT_CREDIT_HOURS
                )
                course.save()

    def add_student_grades_gpa(self):
        """
        Add all new grades for each student.
        Calculates and adds gpa
        Registers student in courses
        """
        #TODO: Break up this method

        for entry in self.csv:
            gpa_sum = 0.0
            hours_attempted = 0.0
            student = Student.objects.get(calstudentID=entry[3])
            user = CustomUser.objects.get(student=student)

            for i, grade in enumerate(entry):
                if i > 28 and grade != "":
                    course = Course.objects.get(title=self.columns[i])
                    grade = Grade.objects.create(
                        student=user,
                        course=course,
                        grade=grade
                    )
                    grade.save()
                    student.courses.add(course)
                    gpa_sum += (self.get_gpa_value(int(grade.grade))) * c.DEFAULT_CREDIT_HOURS
                    hours_attempted += c.DEFAULT_CREDIT_HOURS
    
            gpa = round((gpa_sum/hours_attempted), 2)
            gpa = Gpa.objects.create(
                student=user,
                gpa=gpa
            )
            gpa.save()



    def get_gpa_value(self, grade):

        if grade >= 90:
            grade = 'A'
        elif grade < 90 and grade >= 80:
            grade = 'B'
        elif grade < 80 and grade >= 70:
            grade = 'C'
        elif grade < 70 and grade >= 60:
            grade = 'D'
        else:
            grade = 'F'

        gpa_values = {
            'A': 4.0,
            'B': 3.0,
            'C': 2.0,
            'D': 1.0,
            'F': 0.0
        }

        return gpa_values[grade]


def parse_csv_file(my_csv):

    with open(f'./media/csv/{my_csv}', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        #skip to first row with student information
        next(csv_reader)
        next(csv_reader)
        next(csv_reader)

        csv_reader = list(csv_reader)
        subjects = csv_reader[2]
        name = 2
        calstudentID = 3
        stop = False

        for entry in csv_reader:
            if stop:
                break
            print(f'Student: {entry[name]}')
            if Student.objects.filter(calstudentID=entry[calstudentID]).exists():
                print('found!')
            else:
                student = CustomUser.objects.create_user(email='student2@gmail.com', password=c.DEFAULT_PASSWORD)
                # student.make_new_student(
                #     is_iep = entry[is_iep],
                #     other_stuff=entry[other_stuff]
                # )
                # student.is_student = True
                # student.save()
            # student = Student.object.get(calstudentID=entry[calstudentID])
            # if student.exsists():
            #     print('found student')
            # else:
            #     print('need to add student to database')


            for i, field in enumerate(entry):
                if field != "":
                    if i > 10:
                        print(f'grade: {field} in {subjects[i]}')
            print('\n\n\n')
            stop = True


# all students should be added already
# when we loop through, we locate the student. If a student cannot be found, pop up window that the student needs to be added (build a list of missing students)
# if field is greater than ten and not emtpy, add that grade to the database with date
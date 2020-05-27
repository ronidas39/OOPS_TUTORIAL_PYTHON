#how to declare class
from students import student
from db_objects import db_object
while(1):
    user_input=input('press 1 to input student records in course db')
    if(user_input=='1'):
        student_name=input('please enter the student full name')
        course_name=input('please enter the course name')
        grade=input('please enter the grade for student')    
        student1=student(student_name,course_name,grade)
        db_object1=db_object('course_db','course',student1.get_sname(),student1.get_cname())
        if(db_object1.insert_into_collection()=='created'):
         print(f"{student1.get_sname()} has been enrolled to {student1.get_cname()}")
        else:
            print(f"{student1.get_sname()} has not been enrolled to {student1.get_cname()}")
    else:
        print('programm will be terminated now')
        exit()


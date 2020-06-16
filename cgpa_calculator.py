
#CGPA calculator

cgpa=0
semester =sem= int(input("Enter the number of semesters to be calaculated for: "))
while semester >0:
    Total_subject = int(input("Enter the total course taken: "))
    tnu=0
    course_unit=0
    course_number=1
    while (Total_subject>0):
        subject = str(input (f"Enter course {course_number} title or course code: "))
        unit = int(input (f"Enter the course unit in {subject}: "))
        grade = int(input (f"Enter your score in {subject}: "))
        if (grade >= 70 and grade <=100):
            print (f'{grade}A')
            point = 5
        elif (grade >=60 and grade <70):
            print (f'{grade}B')
            point = 4
        elif (grade >=50 and grade <60):
            print(f'{grade}C')
            point = 3
        elif (grade >=45  and grade <50):
            print(f'{grade}D')
            point = 2
        elif (grade >=40 and grade <45):
            print(f'{grade}E')
            point = 1
        elif (grade>=0 and grade <40):
            print(f'{grade}F')
            point = 0
        else:
            print('Incorrect input. Enter number from 0-100')
            continue
        total_unit_product = point*unit
        tnu = tnu +total_unit_product
        course_unit=unit+course_unit
        course_number+=1
        Total_subject -=1
        
    gpa = tnu/course_unit
    print ('Your GPA is: ', gpa)
    cgpa = (gpa+cgpa)
    semester -=1
cgpa1= float (cgpa/2)
print('Your CGPA is ', cgpa)
                

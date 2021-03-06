import random
students = ['student'+str(i) for i in range(1, 101)]

faculties  = [('Mathematics', 'Murali Krishna'), ('Telugu', 'Amarnath'), ('English', 'Samuel'),
              ('Social', 'Krishna Reddy'), ('Physics', 'Raja Gopal'), ('Chemistry', 'Ravi') ]

with open('student_marks.csv', 'w') as f:

    for student in students:
        for sub, fac in faculties:
            f.write(','.join([student, sub, str(random.sample(range(1, 101), 1)[0])]) + '\n')

with open('subject_faculty.csv', 'w') as f:
    for rec in faculties:
        f.write(','.join(rec) + '\n')


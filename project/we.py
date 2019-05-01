students_marks = []
with open('student_marks.csv') as f:
	for line in f:
		columns = line.split(',')
		columns[-1] = int(columns[-1].rstrip('\n'))
		students_marks.append(tuple(columns))

subject_faculty = []
with open('subject_faculty.csv') as k:
	for line in k:
		columns = line.split(',')
		columns[-1] = columns[-1].rstrip('\n')
		subject_faculty.append(tuple(columns))

def highest_student_count_more_than_90percent():
	d = {}
	i = 0
	students_marks_copy = students_marks
	for x in students_marks_copy:
		student, subject, marks = x
		if (marks > 90):
			if subject not in d:
				d[subject] = 1
			else:
				d[subject] += 1
	high_subject = max(d.items(), key=lambda x:x[1])
	subject_faculty_dict = dict(subject_faculty)
	print((subject_faculty_dict[high_subject[0]]))
	print()

def highest_student_count_more_than_40percent():
	d = {}
	i = 0
	students_marks_copy = students_marks
	for x in students_marks_copy:
		student, subject, marks = x
		if (marks > 40):
			if subject not in d:
				d[subject] = 1
			else:
				d[subject] += 1
	high_subject = max(d.items(), key=lambda x:x[1])
	subject_faculty_dict = dict(subject_faculty)
	print((subject_faculty_dict[high_subject[0]]))
	print()

def highest_student_count_less_than_40percent():
	d = {}
	i = 0
	students_marks_copy = students_marks
	for x in students_marks_copy:
		student, subject, marks = x
		if (marks <= 90):
			if subject not in d:
				d[subject] = 1
			else:
				d[subject] += 1
	high_subject = max(d.items(), key=lambda x:x[1])
	subject_faculty_dict = dict(subject_faculty)
	print((subject_faculty_dict[high_subject[0]]))
	print()

def maximum_total():
	d = {}
	students_marks_copy = students_marks
	for x in students_marks_copy:
		student, subject, marks = x
		if student not in d:
			d[student] = marks
		else:
			d[student] += marks
	print(max(d.items(), key=lambda x:x[1]))
	print()

def highest_maths():
	d = {}
	students_marks_copy = students_marks
	for x in students_marks_copy:
		student, subject, marks = x
		if subject == 'Mathematics':
			d[student] = marks
	print(max(d.items(), key=lambda x:x[1]))
	print()

def avg_mark_subject():
	d = {}
	l = []
	students_marks_copy = students_marks
	for x in students_marks_copy:
		student, subject, marks = x
		if marks > 40:
			if subject not in d:
				d[subject] = marks
			else:
				d[subject] += marks
		if student not in l:
			l.append(student)
	for x in d:
		print (x , d[x]/len(l))
	print()

def minimum_total():
	d = {}
	students_marks_copy = students_marks
	for x in students_marks_copy:
		student, subject, marks = x
		if student not in d:
			d[student] = marks
		else:
			d[student] += marks
	print(min(d.items(), key=lambda x:x[1]))
	print()

highest_student_count_more_than_90percent()
highest_student_count_more_than_40percent()
highest_student_count_less_than_40percent()
maximum_total()
highest_maths()
avg_mark_subject()
minimum_total()
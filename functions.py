# CSC 365 Fall 2017
# Andy Tan, Liam Gow, Chris Scarborough

def student(students, lastname, bus=False):
    for s in students:
        if s['StLastName'] == lastname:
            if (bus):
                print('{}, {} - BUS: {}'.format(s['StLastName'], s['StFirstName'], s['Bus']))
            else:
                print('{}, {} - GRADE: {}, TEACHER: {}'.format(s['StLastName'], s['StFirstName'], s['Grade'],
                                                               s['TLastName'], s['TFirstName']))


def teacher(students, lastname):
    for s in students:
        if s['TLastName'] == lastname:
            print('{}, {}'.format(s['StLastName'], s['StFirstName']))


def bus(students, number):
    for s in students:
        if s['Bus'] == number:
            print('{} {} - GRADE: {}, CLASSROOM: {}'.format(s['StFirstName'], s['StLastName'], s['Grade'],
                                                            s['Classroom']))


def grade(students, number, high=False, low=False):
    if low:
        sort = sorted([s for s in students if s['Grade'] == number], key=lambda s: s['GPA'], reverse=False)
        if sort:
            s = sort[0]
            print('{} - GPA: {}, TEACHER: {}, BUS: {}'.format(s['StFirstName'], s['GPA'], s['TLastName'], s['Bus']))

    elif high:
        sort = sorted([s for s in students if s['Grade'] == number], key=lambda s: s['GPA'], reverse=True)
        if sort:
            s = sort[0]
            print('{} - GPA: {}, TEACHER: {}, BUS: {}'.format(s['StFirstName'], s['GPA'], s['TLastName'], s['Bus']))

    else:
        for s in students:
            if s['Grade'] == number:
                print('{}, {}'.format(s['StLastName'], s['StFirstName']))


def average(students, number):
    num_stu = 0
    sum_gpa = 0.0

    for s in students:
        if s['Grade'] == number:
            num_stu += 1
            sum_gpa += float(s['GPA'])

    if num_stu:
        print('{} STUDENTS, AVERAGE GPA: {}'.format(num_stu, sum_gpa / num_stu))


def info(students):
    tally = [0, 0, 0, 0, 0, 0, 0]

    for s in students:
        tally[int(s['Grade'])] += 1

    for t in range(len(tally)):
        print('{}: {}'.format(t, tally[t]))


# students = [{'StLastName': 'DROP', 'StFirstName': 'SHERMAN', 'Grade': 0, 'Classroom': 104, 'Bus': 51, 'GPA': 2.65,
#              'TLastName': 'NIBLER', 'TFirstName': 'JERLENE'}]
#
# student('DROP', bus=True)
# teacher('NIBLER')
# grade(0)
# grade(0, high=True)
# grade(0, low=True)
# bus(51)
# average(0)
# info()
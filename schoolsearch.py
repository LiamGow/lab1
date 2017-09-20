# CSC 365 Fall 2017
# Andy Tan, Liam Gow, Chris Scarborough

import functions
import parse

def schoolsearch(path):
    do_prompt = False

    prompt = "S[tudent]: <lastname> [B[us]]\n" \
             "T[eacher]: <lastname>\n" \
             "B[us]: <number>\n" \
             "G[rade]: <number> [H[igh]]|[L[ow]]\n" \
             "A[verage]: <number>\n" \
             "I[nfo]\n" \
             "Q[uit]\n" \
             "> "

    students = parse.parse(path)

    while(True):
        command = input(prompt if do_prompt else "").replace(":", "")
        args = command.split(" ")

        # Account for comments in tests
        if '#' in args:
            continue
        try:
            opt = args[0][0]
            first = args[1] if len(args) > 1 else None
            second = args[2] if len(args) > 2 else None
        except IndexError:
            continue

        if opt in ["S", "Student"] and 2 <= len(args) < 4 and second in [None, "B", "Bus"]:
            functions.student(students, first, second) # second here is being treated as a boolean
        elif opt in ["T", "Teacher"] and len(args) == 2:
            functions.teacher(students, first)
        elif opt in ["B", "Bus"] and len(args) == 2:
            functions.bus(students, first)
        elif opt in ["G", "Grade"] and 2 <= len(args) < 4:
            functions.grade(students, first, True if second in ["H", "High"] else False, True if second in ["L", "Low"] else False)
        elif opt in ["A", "Average"] and len(args) == 2:
            functions.average(students, first)
        elif opt in ["I", "Info"] and len(args) == 1:
            functions.info(students)
        elif opt in ["Q", "Quit"] and len(args) == 1:
            return 0
        else:
            print("Invalid command")



if __name__ == "__main__":
    schoolsearch("students.txt")
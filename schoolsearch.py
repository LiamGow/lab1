import functions
import parse

def schoolsearch(path):
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
        command = input(prompt)
        args = command.split(" ")

        try:
            opt = args[0][0]
            first = args[1] if len(args) > 1 else None
            second = args[2] if len(args) > 2 else None
        except IndexError:
            continue

        if opt in ["S", "Student"]:
            functions.student(students, first, second) # second here is being treated as a boolean
        elif opt in ["T", "Teacher"]:
            functions.teacher(students, first)
        elif opt in ["B", "Bus"]:
            functions.bus(students, first)
        elif opt in ["G", "Grade"]:
            functions.grade(students, first, True if second in ["H", "High"] else False, True if second in ["L", "Low"] else False)
        elif opt in ["A", "Average"]:
            functions.average(students, first)
        elif opt in ["I", "Info"]:
            functions.info(students)
        elif opt in ["Q", "Quit"]:
            return 0
        else:
            print("Invalid command")



if __name__ == "__main__":
    schoolsearch("students.txt")
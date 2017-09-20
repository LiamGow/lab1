# CSC 365 Fall 2017
# Andy Tan, Liam Gow, Chris Scarborough

def parse(path):
    try:
        with open(path, 'r') as csv:
            students = []
            for line in csv.readlines():
                parts = line[:-1].split(",")
                try:
                    if len(parts) != 8:
                        raise IndexError
                    students.append({"StLastName":parts[0], "StFirstName":parts[1], "Grade":parts[2], "Classroom":parts[3],
                                     "Bus":parts[4], "GPA":parts[5], "TLastName":parts[6], "TFirstName":parts[7]})
                except IndexError:
                    print("Malformed line")
                    return None
                    # exit(3)

            return students

    except IOError:
        print("Filepath invalid")
        return None
        # exit(2)

if __name__ == "__main__":
    print(parse("students.txt"))

    print(parse("x.txt"))
    print(parse("studets.txt"))
    print(parse("studennts.txt"))
    print(parse("studenewlinets.txt"))
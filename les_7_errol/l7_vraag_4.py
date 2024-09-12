from students_classrooms import students_per_classroom


def get_excellent_student(student):
    uitmuntend_counter = 0
    goed_counter = 0

    for result in student["resultaten"].values():
        if result == "onvoldoende":
            continue
        elif result == "uitmuntend":
            uitmuntend_counter += 1
            if uitmuntend_counter == 2:
                return student
        elif result == "goed":
            goed_counter += 1
            if goed_counter == 4:
                return student
        else:
            continue

    return None


def get_excellent_students(all_students):
    exc_students = []
    for student in all_students:
        exc_student = get_excellent_student(student)
        if not exc_student is None:
            exc_students.append(exc_student)
        else:
            continue
    return exc_students


def get_most_excellent_classroom(students_per_classroom):
    classrooms = {}
    for classroom in students_per_classroom:
        students = get_students(students_per_classroom[classroom])
        total_students = len(students_per_classroom[classroom])
        ex_students = len(get_excellent_students(students))
        classrooms[classroom] = (ex_students / total_students)

    most_excellent_classroom = get_best_classroom(classrooms)
    return most_excellent_classroom


def get_best_scoring_classroom(students_per_classroom):
    classrooms = {}
    for classroom in students_per_classroom:
        students_score = 0
        students = get_students(students_per_classroom[classroom])
        for student in students:
            student_score = get_score(student)
            students_score += student_score
        avg_score = students_score / len(students_per_classroom[classroom])
        classrooms[classroom] = avg_score

    best_scoring_classroom = get_best_classroom(classrooms)
    return best_scoring_classroom


def get_score(student):
    score = 0
    for result in student["resultaten"].values():
        if result == "voldoende":
            score += 2
            continue
        elif result == "goed":
            score += 3
            continue
        elif result == "uitmuntend":
            score += 4
            continue
        else:
            continue
    return score


def get_best_classroom(classrooms):
    best_classroom = ""
    best_classroom_score = 0
    for classroom, score in classrooms.items():
        if score > best_classroom_score:
            best_classroom = classroom
            best_classroom_score = score

    return best_classroom


def get_all_students(students_per_classroom):
    all_students = []
    for classroom in students_per_classroom:
        for student in students_per_classroom[classroom]:
            all_students.append(student)
    return all_students


def get_students(classroom):
    students = []
    for student in classroom:
        students.append(student)
    return students


def get_failed_students(all_students, minimum_score = 4):
    failed_students = {}
    for student in all_students:
        student_score = get_score(student)
        if student_score < minimum_score:
            failed_students[student["naam"]] = student["resultaten"]
    return failed_students


def print_rapport(students_per_classroom):
    print("------ Rapport 02-09-2023 ------")
    print("Excellente studenten:")
    all_students = get_all_students(students_per_classroom)
    all_excellent_students = get_excellent_students(all_students)

    for student in all_excellent_students:
        print(f"\t-{student['naam']}")
    print()

    print("Klas met de meeste excellente studenten:")
    print(f"\t-{get_most_excellent_classroom(students_per_classroom)}")
    print()

    print("Klas met de hoogste scores gemiddeld:")
    print(f"\t-{get_best_scoring_classroom(students_per_classroom)}")
    print()

    print("Studenten met inhaalopdracht:")
    all_failed_students = get_failed_students(all_students)
    for student, resultaten in all_failed_students.items():
        print(f"\t-{student}")
        for workplace, grade in resultaten.items():
            print(f"\t\t{workplace}: {grade}")
        print()


print_rapport(students_per_classroom)
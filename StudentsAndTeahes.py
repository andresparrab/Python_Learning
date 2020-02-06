lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}


# Add your function below!
def average(numbers):
    total = sum(numbers)
    result = float(total) / (len(numbers))
    return result


def get_average(student):
    homework = 0.1 * average(student["homework"])
    quizzes = 0.3 * average(student["quizzes"])
    tests = 0.6 * average(student["tests"])
    return homework + quizzes + tests


def get_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

students=[lloyd,alice,tyler]
def get_class_average(class_list):
    result = []
    for student in class_list:
        result.append(get_average(student))
        # print(result)
        return average(result)



print(get_letter_grade(get_average(alice)))
# print(get_class_average(students))
print(get_class_average(students))
print(get_letter_grade(get_class_average(students)))



def gradingStudents(grades):
    result = []
    for grade in grades:
        if grade < 38:
            result.append(grade)
        else:
            next_multiple = ((grade // 5) + 1) * 5
            if next_multiple - grade < 3:
                result.append(next_multiple)
            else:
                result.append(grade)
    return result
n = int(input())
grades = []

for _ in range(n):
    grades.append(int(input()))

rounded_grades = gradingStudents(grades)

for grade in rounded_grades:
    print(grade)

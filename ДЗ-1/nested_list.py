n = int(input())
students = []
points = []

for _ in range(n):
    name = input()
    point = float(input())
    student = [name, point]
    students.append(student) 
    points += [point]

second_score = sorted(set(points))[1]

second_score_students = []
print(second_score)
for student in students:
    if (student[1] == second_score):
        second_score_students.append(student[0])

second_score_students.sort()

print(*second_score_students, sep='\n')
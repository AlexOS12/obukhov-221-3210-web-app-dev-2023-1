n = int(input())
students = {}

scScore = mnScore = float('inf')

for _ in range(n):
    name = input()
    score = float(input())
    students.update({name : score})
    if score < mnScore:
        scScore = mnScore
        mnScore = score
    elif score < scScore and score != mnScore:
        scScore = score

if scScore == float('inf') and mnScore != float('inf'):
    scScore = mnScore

secondScoreStudents = []

for i in students.items():
    if i[1] == scScore:
        secondScoreStudents.append(i[0])

print(*sorted(secondScoreStudents), sep='\n')
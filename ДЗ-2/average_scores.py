def compute_average_scores(scores : list[list[float]]) -> tuple[float]:
    if len(scores) == 0 or len(scores[0]) == 0:
        return tuple()

    avg_scores = [0  for i in range(len(scores[0]))]

    for student in scores:
        for i in range(len(student)):
            avg_scores[i] += student[i]

    avg_scores = [i / len(scores) for i in avg_scores]

    return tuple(avg_scores)

if __name__ == "__main__":
    n, x = list(map(int, input().split()))
    students = []

    for i in range(x):
        students.append(list(map(float, input().split())))

    avg_scores = compute_average_scores(students)

    for score in avg_scores:
        print(f"{score:.1f}")
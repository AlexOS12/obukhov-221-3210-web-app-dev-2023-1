import random


def circle_square_mk(r: float | int, n: int) -> float:
    in_circle_pts = 0
    if r <= 0: return 0

    for i in range(n):
        x, y = random.uniform(-r, r), random.uniform(-r, r)
        d = (x ** 2 + y ** 2) ** 0.5

        if d <= r:
            in_circle_pts += 1
    L  = (2 * r) ** 2
    sq = L * in_circle_pts / n
    return sq


if __name__ == "__main__":
    r = float(input())
    n = int(input())

    print(circle_square_mk(r, n))

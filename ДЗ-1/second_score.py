n = int(input())
a = list(map(int, input().split()))

mxScore = scScore = -float('inf')

for i in a:
    if i > mxScore:
        scScore = mxScore
        mxScore = i
        if scScore == -float('inf'):
            scScore = mxScore
    elif i > scScore and i != mxScore:
        scScore = i

print(scScore)
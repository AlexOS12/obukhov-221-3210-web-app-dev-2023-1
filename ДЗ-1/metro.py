n = int(input())
passengers = []

for i in range(n):
    timeA = int(input())
    timeB = int(input())

    passengers.append([timeA, timeB])

t = int(input())

passCount = 0

for i in passengers:
    if i[0] <= t <= i[1]:
        passCount += 1
    
print(passCount)
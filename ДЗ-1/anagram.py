a = input().lower()
b = input().lower()

fl = True

for i in set(a):
    if a.count(i) != b.count(i):
        fl = False
        break

print("YES" if fl else "NO")
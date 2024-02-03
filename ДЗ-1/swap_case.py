s = input()
ns = ""

for c in s:
    if c.islower():
        ns += c.upper()
    else:
        ns += c.lower()

print(ns)
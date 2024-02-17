s = input()

vowels = "AEIOU"
ln = len(s)
stuart = kevin = 0

for i in range(ln):
    if s[i] in vowels:
        kevin += ln - i
    else:
        stuart += ln - i

print("Кевин" if kevin > stuart else "Стюарт", max(kevin, stuart))
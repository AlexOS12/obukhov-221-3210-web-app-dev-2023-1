with open("products.csv", encoding="utf-8") as file:
    csv = file.readlines()[1:]

adult = senior = child = 0

for line in csv:
    prices = line.split(",")

    adult += float(prices[1])
    senior += float(prices[2])
    child += float(prices[3])

print(f"{adult:.2f} {senior:.2f} {child:.2f}")

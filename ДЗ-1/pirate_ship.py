n, m = list(map(int, input().split()))
loads = []

for i in range(m):
    name, weight, price = input().split()
    weight, price = int(weight), int(price)
    # штука, цена, вес, цена за ед веса (больше = лучше)
    loads.append((name, weight, price, price / weight))

loads = sorted(loads, key=lambda x: x[3], reverse=True)
taken_load = []

for i in loads:
    if n <= 0:
        break
    
    max_amount = min(i[1], n)
    taken_load.append((i[0], max_amount, i[2] * (max_amount / i[1])))
    n -= max_amount

for name, weight, price in taken_load:
    weight = f"{weight:.2f}" if weight % 1 else int(weight)
    price = f"{price:.2f}" if price % 1 else int(price)
    print(f"{name} {weight} {price}")

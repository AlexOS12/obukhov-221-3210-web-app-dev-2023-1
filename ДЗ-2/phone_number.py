def wrapper(f):
    def fun(l):
        phones = f(l)
        for i in range(len(phones)):
            digs = list(str(phones[i]))
            if len(digs) == 11:
                del digs[0]
            digs = ''.join(digs)
            phone = f"+7 ({digs[:3]}) {digs[3:6]}-{digs[6:8]}-{digs[8:10]}"
            phones[i] = phone
        return phones
    return fun

@wrapper
def sort_phone(l):
    return sorted(l)

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    print(*sort_phone(l), sep='\n')

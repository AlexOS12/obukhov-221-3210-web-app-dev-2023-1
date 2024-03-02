import re

def fun(s : str) -> bool:
    """return True if s is a valid email, else return False"""
    # regEx = re.compile(r'^[a-zA-Z0-9\-\_]@^[a-zA-Z0-9\-\_].^[a-zA-Z0-9\-\_]')
    regEx = re.compile(r'[a-zA-Z0-9\-\_]+@[a-zA-Z0-9\-\_]+\.[a-zA-Z0-9\-\_]{1,3}$')
    return re.fullmatch(regEx, s)


def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)

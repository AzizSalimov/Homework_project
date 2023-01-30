def get_info():
    res = []
    try:
        with open('homework.txt', 'r', encoding='utf8') as f:
            file = f.readlines()
    except FileNotFoundError as e:
        return e
    return file

def get():
    info = get_info()
    for i in info:
        if 'name' in i:
            yield i.split('=')[1]


count = iter(get())
print(next(count))
print(next(count))
print(next(count))
print(next(count))
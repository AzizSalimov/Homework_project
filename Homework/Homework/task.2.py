def get_info():
    res = []
    try:
        with open('Homwork.txt', 'r', encoding='utf8') as f:
            file = f.read()
    except FileNotFoundError as e:
        return e
    return file



def generatot():
    itr = get_info()
    for i in itr:
        yield i

tt = generatot()
print(next(tt))
print(next(tt))
print(next(tt))
print(next(tt))
print(next(tt))
print(next(tt))
print(next(tt))
print(next(tt))
print(next(tt))
print(next(tt))
print(next(tt))
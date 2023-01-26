# 1
def task1(text) -> list:
    l = []
    for i in range(len(text)):
        if text[i] == 'a':
            l.append(i)

    return l


print(task1('assalom'))

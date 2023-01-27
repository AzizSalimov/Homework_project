def generator():
    nam = 2
    while True:
        for i in range(2, nam):
            if nam % i == 0:
                break
        else:
            yield nam
        nam += 1


generator_ = generator()
print(next(generator_))
print(next(generator_))
print(next(generator_))
print(next(generator_))
print(next(generator_))
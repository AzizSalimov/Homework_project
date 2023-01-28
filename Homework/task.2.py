# def generator():
#     count = 2
#     while True:
#         for i in range(2, count):
#             if count % i == 0:
#                 break
#         else:
#             yield count
#         count += 1
#
#
# generator_ = generator()
# print(next(generator_))
# print(next(generator_))
# print(next(generator_))
# print(next(generator_))
# print(next(generator_))
#
#
#
def generator():
    for i in range(2, 100):
        for f in range(2, i):
            if i % f == 0:
                break

        else:
            yield i


count = generator()

for i in range(15):
    print(next(count))


def generator(func):
    def generator_(a, b):
        return func(a, b) * 2
    return generator_
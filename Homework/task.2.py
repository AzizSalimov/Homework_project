# def generator():
#     nam = 2
#     while True:
#         for i in range(2, nam):
#             if nam % i == 0:
#                 break
#         else:
#             yield nam
#         nam += 1
#
#
# generator_ = generator()
# print(next(generator_))
# print(next(generator_))
# print(next(generator_))
# print(next(generator_))
# print(next(generator_))



def generator():
    for i in range(2, 1000):
        for f in range(2, i):
            if i % f == 0:
                break

        else:
            yield i


count = generator()

for i in range(15):
    print(next(count))
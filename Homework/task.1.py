# class Numbers:
#     def __init__(self, count = 0):
#         self.count = count
#
#     def __iter__(self):
#         self.n = 1
#         return self
#
#     def __next__(self):
#             number = 2 * self.n
#             self.n += 1
#             return number
#
#
#
# numbers = Numbers()
# iterator = iter(numbers)
#
# numbers_ = Numbers()
# iterator_ = iter(numbers)
#
#
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
#
#
def generator(get):
    count = 0
    while True:
        yield get
        get *= count


a = generator(5)

print(next(a))
print(next(a))
print(next(a))

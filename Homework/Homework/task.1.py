# def itrator():
#     for i in range(1, 20):
#         for j in range(i):
#             if i % 2 == 0:
#                     print(f"-{i}")
#             break
#
#         else:
#             yield i
#
#
#
# count = itrator()
#
# for _ in range(20):
#     print(next(count))
#



def generator__():
    for i in range(1, 21):
         if i%2==0:
          yield f"-{i}"
         else:
            yield i
conunt = iter(generator__())

print(next(conunt))
print(next(conunt))
print(next(conunt))
print(next(conunt))
print(next(conunt))
print(next(conunt))
print(next(conunt))

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")
#
#
# def decoration(nam):
#     def decoration_(a, b):
#         try:
#             return nam(a, b)
#
#         except ZeroDivisionError:
#             print("Iltimos son kiriting")
#
#     return decoration_
#
#
# def decorator(num):
#     def external(a, b):
#         if b % 2 == 0:
#             b += 1
#         return num(a, b)
#
#     return external
#
#
# @decoration
# def deco(a, b):
#     if a % 2 == 0:
#         return a + b
#
#
# @decoration
# def running_away(a, b):
#     if a % 2 == 0:
#         return a + b
#
#
# print(deco(1, 3))
# print(running_away(2, 6))
#

def generator(func):
    def generator_(*args):

        for arg in args:
            if arg % 2 != 0:
                return 'Please multiple only even numbers!'

        return func(*args)

    return generator_


@generator
def gene_(a, b, d, e):
    return a * b * d * e


@generator
def gene__(a, b):
    return a + b


print(gene__(3, 4))
print(gene_(2, 4, 6, 8))

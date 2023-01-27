# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")


def decoration(nam):
    def decoration_(a, b):
        try:
            return nam(a, b)

        except ZeroDivisionError:
            print("Iltimos son kiriting")


    return decoration_


def decorator(num):
    def external(a, b):
        if b % 2 == 0:
            b += 1
        return num(a, b)

    return external


@decoration
def deco(a, b):
    if a % 2 == 0:
        return a + b


@decoration
def running_away(a, b):
    if a % 2 == 0:
        return a + b


print(deco(1, 3))
print(running_away(2, 6))

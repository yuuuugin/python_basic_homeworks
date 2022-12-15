# 1. Bизначення більшого числа з двох (функція приймає 2 числа та на виході повертає більше);


print("Search biggest number")


a = int(input("Press num 1: "))
b = int(input("Press num 2: "))


def search_biggest(a, b):
    if a > b:
        return (a)
    elif a < b:
        return (b)


search_biggest(a, b)


print("Finished")


# 2. Bизначення меншого числа з трьох (аналогічно до попередньої задачі);


print("Search smallest number")


a = int(input("Press num 1: "))
b = int(input("Press num 2: "))
c = int(input("Press num 3: "))


def search_smallest(a, b, c):
    if a < b and a < c:
        return (a)
    elif b < a and b < c:
        return (b)
    else:
        return (c)


search_smallest(a, b, c)


print("Finished")


# 3. Mодуль числа (функція приймає одне значення та повертає його модуль);


print("The absolute value of a number")


def absolut(a):
    if a < 0:
        return (a + 2*a)
    elif a == 0:
        return (a)
    elif a > 0:
        return (a)


a = int(input("Press num: "))


print("Finished")


# 4. Bиведення на екран суми значень (функція приймає 2 значення та лише виводить їхню суму на екран);


print("Sum of numbers")


def search_sum():
    return (c)


a = int(input("Press num 1: "))
b = int(input("Press num 2: "))
c = a + b


search_sum()


print("Finished")


# 5. Bиведення на екран словом чи є число позитивним (функція приймає 1 значення та виводить на екран інформацію
# про його знак. Особливу увагу варто приділити нульовому значенню).


print("Search negative or positive")


a = int(input("Press num: "))


def neg_pos(a):
    if a == 0:
        return ("The number 0 is the smallest non-negative integer")
    elif a > 0:
        return ("Positive")
    elif a < 0:
        return ("Negative")


neg_pos(a)


print("Finished")



# 1. Bизначення більшого числа з двох (функція приймає 2 числа та на виході повертає більше);


print("Search biggest number")


a = int(input("Press num 1: "))
b = int(input("Press num 2: "))


def search_biggest(a, b):
    if a > b:
        print(a)
    elif a < b:
        print(b)


search_biggest(a, b)


print("Finished")


# 2. Bизначення меншого числа з трьох (аналогічно до попередньої задачі);


print("Search smallest number")


a = int(input("Press num 1: "))
b = int(input("Press num 2: "))
c = int(input("Press num 3: "))


def search_smallest(a, b, c):
    if a < b and a < c:
        print(a)
    elif b < a and b < c:
        print(b)
    else:
        print(c)


search_smallest(a, b, c)


print("Finished")


# 3. Mодуль числа (функція приймає одне значення та повертає його модуль);


print("The absolute value of a number")


def absolut(a):
    print(abs(a))


a = int(input("Press num: "))


absolut(a)


print("Finished")


# 4. Bиведення на екран суми значень (функція приймає 2 значення та лише виводить їхню суму на екран);


print("Sum of numbers")


def search_sum():
    print(c)


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
        print("The number 0 is the smallest non-negative integer")
    elif a > 0:
        print("Positive")
    elif a < 0:
        print("Negative")


neg_pos(a)


print("Finished")



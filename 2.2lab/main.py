def IsLeapYear(Y):
    return Y % 4 == 0 and (Y % 100 != 0 or Y % 400 == 0)
a = IsLeapYear(2025)
print(a)

import math

def add_fractions(frac1, frac2):
    num1, den1 = frac1
    num2, den2 = frac2
    lcm = den1 * den2 // math.gcd(den1, den2)
    numerator = num1 * (lcm // den1) + num2 * (lcm // den2)
    gcd = math.gcd(numerator, lcm)
    return (numerator // gcd, lcm // gcd)

def subtract_fractions(frac1, frac2):
    num1, den1 = frac1
    num2, den2 = frac2
    lcm = den1 * den2 // math.gcd(den1, den2)
    numerator = num1 * (lcm // den1) - num2 * (lcm // den2)
    gcd = math.gcd(abs(numerator), lcm)
    return (numerator // gcd, lcm // gcd)

def multiply_fractions(frac1, frac2):
    num1, den1 = frac1
    num2, den2 = frac2
    numerator = num1 * num2
    denominator = den1 * den2
    gcd = math.gcd(numerator, denominator)
    return (numerator // gcd, denominator // gcd)

if __name__ == "__main__":
    frac_a = (1, 2)
    frac_b = (1, 3)
    print(f"Сложение: {frac_a} + {frac_b} = {add_fractions(frac_a, frac_b)}")
    print(f"Вычитание: {frac_a} - {frac_b} = {subtract_fractions(frac_a, frac_b)}")
    print(f"Умножение: {frac_a} * {frac_b} = {multiply_fractions(frac_a, frac_b)}")

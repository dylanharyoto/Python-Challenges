def mf(a1, b1, a2, b2):
    def gcd(num1, num2):
        while num2 != 0:
            num1, num2 = num2, num1 % num2
        return num1
    # 6,1, 6, -3
    # -6, -2, -2, -3
    # -41, 5, 28, -40
    # 6, 19, 45, -14
    a = a1 * a2
    b = b1 * b2
    gc = gcd(a, b)
    a = int(a / gc)
    b = int(b / gc)
    return a, b
# a1, b1, a2, b2 = -41, 5, 28, -40
# a, b = mf(a1, b1, a2, b2)
# sign1 = (1 if a1 >= 0 else -1) * (1 if b1 >= 0 else -1)
# sign2 = (1 if a2 >= 0 else -1) * (1 if b2 >= 0 else -1)
# sign = (1 if a1 >= 0 else -1) * (1 if b1 >= 0 else -1)
# fn1 = f"{sign1 * abs(a1)}/{abs(b1)}" if abs(b1) != 1 else f"({sign1 * abs(a1)})"
# fn2 = f"{sign2 * abs(a2)}/{abs(b2)}" if abs(b2) != 1 else f"({sign1 * abs(a2)})"
# fn = f"{sign * abs(a)}/{abs(b)}" if abs(b) != 1 else f"({sign1 * abs(a)})"
# print(f"({fn1}) x ({fn2}) = ({fn})")

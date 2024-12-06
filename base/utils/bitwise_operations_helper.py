class BitwiseMathClass:
    def __init__(self, value):
        self.value = value & 0xFF

    def __repr__(self):
        return f"({self.value:08b}) {self.value}"

    def __and__(self, other):
        a = self.value
        b = other.value
        while b != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry & 0xFF
        result = BitwiseMathClass(a & 0xFF)
        return result

    def __sub__(self, other):
        b = other.value
        b_neg = (~b + 1) & 0xFF
        return self & BitwiseMathClass(b_neg)

    def __mul__(self, other):
        a = self.value
        b = other.value
        result = 0
        while b > 0:
            if b & 1:
                result ^= a
            a = (a << 1) & 0xFF
            b >>= 1
        return BitwiseMathClass(result)

    def __truediv__(self, other):
        dividend = self.value
        divisor = other.value
        quotient = 0
        while dividend >= divisor:
            dividend = (dividend - divisor) & 0xFF
            quotient += 1
        return BitwiseMathClass(quotient), BitwiseMathClass(dividend)


num1 = BitwiseMathClass(5)
num2 = BitwiseMathClass(3)
res = num1 & num2
res2 = num1 - num2
res3 = num1 * num2
res4 = num1 / num2

print(res)
print(res2)
print(res3)
print(res4)

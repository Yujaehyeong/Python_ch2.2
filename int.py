a = 23
print(a, type(a))
print(isinstance(a, int)) # a가 int 형태인지 체크

# 2진, 10진, 16진, 8진 상수(literal)
b = 0b1101
c = 0o23
d = 0x23
print(b, c, d)

# 3.x int long 1 합쳐졌다. (무한대 표현범위)
e = 2 ** 1024
print(e)
print(type(e))

#변환변수
print(oct(38))
print(hex(38))
print(bin(38))

a = 1.2
print(a, type(a))
print(isinstance(a, float))

b = 2.0
print(type(b))
print(b.is_integer())

b = 3e3
c = -0.2e-4
print(b, c)


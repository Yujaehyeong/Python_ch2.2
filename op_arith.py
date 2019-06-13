print(2  * 3)
print(2  + 3)
print(2  - 3)
print(2  / 3) # 나눗셈은 소숫점을 생략없이 그대로 나눈다
print(2  / 3.0)
print(2.0  / 3.0)


# //(몫) **(지수승), %(나머지)
print(2 // 3)
print(2 ** 3)
print(2 % 3)

# 몫, 나머지 동시에 값을 반환
result, last = divmod(2, 3) # 2개의 값을 반환하는 것이 아니라 tuple 형태를 반환
print(result, last)

t = divmod(2, 3)
print(t, type(t))

print(-2 + 3 * 4)
print(-(2 + 3) * 4)

print(4/2*2)

# 결합순서 주의!!
print((2 ** 3) **4)
print(2 ** 3 ** 4)
print(2 ** (3 ** 4))


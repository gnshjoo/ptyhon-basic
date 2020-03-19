# Chapter 04 - 2
# 파이썬 반복문
# For 실습

# 코딩의 핵심
# for in <collection>
#       <Loop body>

for v1 in range(10): # 0 ~ 9
    print('v1 is :', v1)

print()

for v2 in range(1, 11): # 1 ~ 10
    print('v2 is :', v2)

print()

for v3 in range(1, 11, 2): # 1 ~ 10까지 2 건너뜀
    print('v3 is :', v3)

print()
# 1 ~ 1000 합
sum1 = 0
for v4 in range(1, 1001):
    sum1 += v4
print(sum1)

print()

print('1 ~ 1000 Sum:', sum(range(1,1001)))

print('1 ~ 1000 4의 배수의 함 :', sum(range(4, 1001, 4)))


# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip 

# Ex1
names = ['Kim', 'Park', 'Cho', 'Choi', 'Yoo']

for name in names:
    print('You are : ',name)
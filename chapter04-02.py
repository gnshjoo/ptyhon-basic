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

# Ex 2
lotto_numbers = [11, 19, 21, 28, 36, 37]

for n in lotto_numbers:
    print("Current number : ", n)

# Ex 3
word = "Beaultiful"

for s in word:
    print(s)

# Ex 4
my_info = {
    "name" : "Lee",
    "Age" : 33,
    "city" : "Seoul"
}

for key in my_info:
    print("key : ", my_info.get(key))

for v in my_info.values():
    print('vaules', v)
    

# Ex 5

name = 'FineAppLE'

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())

# break 

numbers = [13, 3, 7, 10, 24, 17, 2, 15, 34, 36, 38, 4]

for number in numbers:
    if number == 34:
        print('Found : 34 !')
        break
    else:
        print('Not Found : ', number)
        continue

# contiune
lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool:
        continue
    else:
        print("Current type", type(v))

# for - else
numbers = [13, 3, 7, 10, 25, 17, 2, 15, 34, 36, 38, 4]

for num in numbers:
    if num == 24:
        print("Found : 24")
        break
else:
    print("Not Found : 24")



# 구구단 출력

for i in range(2, 10):
    for j in range(1, 10):
        print('{:4d}'.format(i*j), end="")
    print()

# 변환 예제
name2 = 'Aceman'

print('Reversed', reversed(name2))
print('List', list(name2))
print('tuple', (tuple(reversed(name2))))
print('set', set(reversed(name2)))
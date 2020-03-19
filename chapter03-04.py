# Chapter 03-4
# 파이썬 튜플
# 리스트와 비교 중요
# 튜플 자료형(순서o, 중복o, 수정x, 삭제x) - 불변
# 중요한 데이터 절대 변경되어서는 안되는 데이터를 튜플로 사용한다.

# 선언
a = ()
b = (1,)
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))

# 인덱싱
print('>>>>>>>>>>>>>>>>>>>>>>')
print('d - ', d[1])
print('d - ', d[1]+d[1]+d[0])
print('d - ', d[-1])
print('e - ', e[-1][1])

# 수정x
# d[0] = 1500

# 슬라이싱
print('d - ', d[0:3])
print('d - ', d[2:])
print('e -', e[2][1:3])

# 튜플 연산
print('>>>>>>>>>>>>>>>>>>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)

# 튜플 함수
a = (5, 3, 2, 1, 4)
print('a -', a)
print('a - ', a.index(3))
print('a count', a.count(2))

# 팩킹 & 언팩킹(Packing, and Unpacking)

# Packing
t = ('foo', 'bar', 'baz', 'qux')

print(t)
print(t[0])
print(t[-1])

# UnPacking1
(x1, x2, x3, x4) = t 
# x1, x2, x3, x4 = t  사용 가능
print(x1, x2, x3, x4)
print(type(x1), type(x2), type(x3), type(x4))

# UnPacking2
t2 = 1, 2, 3 # ()없어도 튜플
t3 = 4, # 튜플
x1, x2, x3 = t2 # UnPacking
x4, x5, x6 = 4, 5, 6 # UnPacking
print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)


# Chapter 03-3
# 파이썬 리스트
# 자료구조에서 중요
# List 자료형 (순서o, 중복o, 수정o, 삭제o)

#선언
a = []
b = list()
c = [70, 675, 85, 120] # len
d = [1000, 10000, "Ace", "Base", "Caption"]
e = [1000, 10000, ["Ace", "Base", "Caption"]]
f = [21.42, 'foobar', 3, 4, False, 3.14159]

# 인덱싱
print(">>>>>>")
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] +d[1]+d[1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1]))

# 슬라이싱
print(">>>>>>>>>>")
print('d- ', d[0:3])
print('d- ', d[2:])
print('e - ', list(e[-1][1:3]))

# 리스트 연산
print(">>>>>>>>>>>>")
print('c + d', c+d)
print("'Test' + c[0]", 'Test' + str(c[0]))

# 값 비교
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])

# Identity(id)
temp = c 
print(id(c))
print(id(temp))

# 리스트 수정, 삭제
print(">>>>>>>>>>>>>>>")
c[2] = 100
print(c)
c[1:2] = ['a', 'b', 'c'] # [['a', 'b', 'c']]
print('c - ', c)
c[1] = ['a', 'b', 'c'] # [['a', 'b', 'c']]
print('c - ', c)
c[1:3] = []
print('c - ', c)
del c[2]
print(c)

# 리스트 함수
a = [5, 4, 3, 2, 1]

print('a - ', a)
a.append(10)
print('a - ', a)
a.sort()
print('a - ', a)
a.reverse()
print('a - ', a)
print('a -', a.index(3), a[3])
a.insert(2, 7)
print('a - ', a)
a.reverse()
print('a - ', a)
# del a[6]
a.remove(10)
print('a - ', a)
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.count(4))
ex = [8,9]
a.extend(ex)
print('a - ', a)

# 삭제 : remove, pop, del

# 반복문 활용
while a:
    data = a.pop()
    print(data)

    
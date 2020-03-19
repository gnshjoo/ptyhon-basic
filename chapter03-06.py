# Chapter03-6
# 집합(set) 특징
# 집합(set) 자료형(순서x, 중복x)

# 선언
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'qux'} # key가 없다면 set이다..
f = {42, 'foo', (1, 2, 3), 3.14159}

print('a - ',type(a), a, 2 in a)
print('b - ',type(b), b, 2 in b)
print('c - ',type(c), c)
print('d - ',type(d), d)
print('e - ',type(e), e)
print('f - ',type(f), f)

# 튜플 변환(set -> tuple)
t = tuple(b)
print('t - ',type(t), t)
print('t - ', t[0], t[1:3])
print()

# 리스트 변환(set -> list)
l = list(c)
l2 = list(e)

print('l - ', type(l), l)
print('l2 - ' , type(l2), l2)

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))


# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('s1 & s2 : ', s1 & s2)
print('s1 & s2 : ', s1.intersection(s2))

print('s1 | s2 : ', s1 | s2)
print('sq | s2 : ', s1.union(s2))

print('s1 - s2 : ', s1 - s2)
print('s1 - s2 : ', s1.difference(s2))

# 중복 원소 확인
print('s1 & s2 : ', s1.isdisjoint(s2)) # False 교집합 , True 없음

# 부분 집합
print(s1.issubset(s2))
print(s1.issuperset(s2))

# 데이터 추가 & 제거
s1 = set([1, 2, 3, 4])

s1.add(5)
print('s1 - ', s1)

s1.remove(2)
print('s1 - ', s1)
# s1.remove(7) # Error

s1.discard(3)
print('s1 - ', s1)
s1.discard(7) # Error 발생하지 않음

s1.clear()
print('s1 - ', s1)

a = [1, 2, 3]
a.clear()
print('a - ', a)

b = {1, 2, }
print(b)
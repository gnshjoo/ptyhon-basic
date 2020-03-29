# Chapter 06 -1
# Python Class
# 객체지향 OOP
# 코드로 재사용이 용이하다
# 개선 / 수정 / 버그 / 사이드 이펙트


# OOP(객체 지향 프로그래밍), self, 인스턴스 메소드, 인스턴스 변수
# class and 인스턴스 차이 이해

# ex1
class Dog: # objeect 상속
    # 클래스 속성
    species = 'fristdog'

    #초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age
# 클래서 정보
print(Dog)

# 인스턴스화
a = Dog("mikey", 2)
b = Dog("baby", 3)
c = Dog("mikey", 2)
# 비교
print(a == b, id(a), id(b))
print(a == c, id(a), id(c))

# 네임스페이스
print('dog1', a.__dict__)
print('dog2', b.__dict__)

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print("{0} is a {1}".format(a.name, a.species))

print(Dog.species)
print(a.species)
print(b.species)

# ex2

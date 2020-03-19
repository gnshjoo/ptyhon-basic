# chapter 02-2
# 파이썬 완전 기초
# 파이썬 변수

#기본 선언
n = 700

# 출력
print(n)
print(type(n)) # 자료형 출력

# 동시 선언
x = y =z = 700 
print(x, y, z)

# 선언
var = 75

# 재선언
var = 'Change Value'

# 출력
print(var)
print(type(var))


# Object References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# ex)1
print(300)
print(int(300))

# ex2
# n -> 777
n = 777

print(n, type(n))
print()

m = n
# m -> 777 <- n

print(m, n)
print(type(m), type(n))
print()

m = 400

print(m, n)
print(type(m), type(n))
print()

# id(identitiy) 확인 : 객체의 고유값 확인
m = 800
n = 655

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

m = 8080
n = 8080
z = 8080
i = 8080

print(id(m))
print(id(n))
print(id(z))
print(id(i))
print(id(m) == id(n) == id(z) == id(i))
print()

# 다양한 변수 선언
# Camel Case : numberOffCollegeGraduates -> Method
# Pascal Case : NumberOfCollegeGraduates -> Class
# Snake Case : nubmer_of_college_graduates -> Python variable
# 예약어는 변수명으로 불가능 [Python reserved words]

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8


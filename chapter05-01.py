# Chapter 05-01
# 파이썬 함수

# 함수 저의 방법
# def function_name(parameter):
#   code

# ex 1
def first_func(w):
    print("Hello, ", w)

word = 'GoodBoy'

first_func(word)

# ex2

def return_func(w1):
    value = "Hello" + str(w1) 
    return value

x = return_func("goodBoy")
print(x)

# ex3 다중 반환

def func_mul(x):
    y1 = x *10
    y2 = x *20
    y3 = x *30
    return y1, y2, y3
x, y, z = func_mul(10)
print(x, y, z)

# tuple return
def func_mul2(x):
    y1 = x *10
    y2 = x *20
    y3 = x *30
    return (y1, y2, y3)
q = func_mul2(10)
print(type(q), q, list(q))

# list return 

def func_mul3(x):
    y1 = x *10
    y2 = x *20
    y3 = x *30
    return [y1, y2, y3]

p = func_mul3(10)

print(type(p), p , set(p))


# dict return
def func_mul4(x):
    y1 = x *10
    y2 = x *20
    y3 = x *30
    return {'v1': y1, 'v2': y2, 'v3': y3}

d = func_mul4(10)

print(type(d), d, d.get('v2'), d.items(), d.keys(), d.values())

# 중요
# *args, **kwargs

# *args(언팩킹)
def args_func(*args):
    for i,v in enumerate(args):
        print('result : {}'.format(i), v)
    print('_________')

args_func('Lee')
args_func('Lee', 'Park')
args_func('Lee', 'Park', 'Kim')

# **kwargs
def kwargs_func(**kwargs):
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print('____________')

kwargs_func(name1='Lee')
kwargs_func(name1='Lee', name2="Park", name3='Kim')

# 전체 혼합
def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)

example(10, 20, 'Lee', 'Kim', 'Park', 'Cho', age1=20, age2=30, age3=40)

# 중첩함수
def nested_func(num):
    def func_in_func(num):
        print(num)
    print('In Func')
    func_in_func(num + 100)

nested_func(100)

# 실행 불가
# fun_in_fun

# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화
# 남발 시 가독성 오히려 감소

# def mul_func(x, y):
#     return x * y
# a =lambda x, y:x*y

# 일반적 함수 -> 할당
def mul_func(x, y):
    return x * y
mul_func_var = mul_func
print(mul_func_var(10, 50))

# 람다 함수 -> 할당
lamda_mul_func = lambda x,y:x*y
print(lamda_mul_func(50,50))

def func_final(x, y, func):
    print(x * y * func(100, 100))

func_final(10, 20, lambda x,y: x * y)


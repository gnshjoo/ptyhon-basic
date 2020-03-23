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
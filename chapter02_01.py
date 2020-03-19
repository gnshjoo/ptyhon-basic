#-*- coding:utf-8 -*-
# Chapter02-1
# 파이썬 완전 기초
# print 사용법
# https://www.python-course.eu/python_fromatted_output.php

# 기본 출력
print('Python Start')
print("python Start!")
print("""python Start!""")
print('''python Start!''')
print()

# separator options
print('python', 'hello', sep=' ')
print()

# end options
print('Welcome to', end='    ')
print('IT News', end='')
print('Web Stile')
print()

# file options
import sys

# sys.stdout -> console 추가
print('Learn Python', file=sys.stdout)
print()

# fortmat used (d:3, s:'python', f: 1.0023)
print('%s %s' % ('one', 'two')) # 정확하게 문자열이 와야함
print('{} {}'.format('one', 2)) # format 함수가 유연하게 처리함
print('{1} {0}'.format('one', 2))

# %s
print('%10s' % ("nice"))
print('{:>10}'.format('nice'))

print('%-10s' % ("nice"))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))
print('{:^10}'.format('nice'))

print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy'))

print('{:10.5}'.format('pythonstudy')) # 공간을 가지고 절삭

# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))


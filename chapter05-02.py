# 파이썬 함수 및 입력
# 파이썬 입력

# Input 사용법
# dfault type(str)

# ex1
# name = input("Enter Your Name")
# grade = input("Enter Your Grade")
# company = input("Enter Your Company Name")
#
# print(name, grade, company)

# ex2
# number = input("Enter number :")
# name = input("Enter name : ")
#
# print('type of number', type(number))
# print('type of name', type(name))

# ex 3 (계산)
first_number = int(input("Enter your number :"))
second_number = int(input("Enter your number :"))

print("total : ", first_number + second_number)

# ex 4
float_number = float(input("Enter a float number : "))

print("input float :", float_number)
print("input type : ", type(float_number))


# 예제5
print("firstname - {0}, LastName - {1}".format(input("Enter first name : "), input("Enter Second Name : ")))
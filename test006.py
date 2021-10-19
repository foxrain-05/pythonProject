def sey_name(name):
    print("안녕 " + name)

def sey_name1(name):
    print(f"안녕 {name}")  #f string
#sey_name("이경태")

def Hello(name,hobby):
    print(f"hi my name is {name},my hobby is {hobby}")

#Hello("이경태","사키")

def info(name,address,phone):
    print(f"name:{name}")
    print(f"address:{address}")
    print(f"phone:{phone}")

#info("경태","경남","010-1234-1234")

def hello(name,age):
    print(f"Hi, {name}, you are {age} years old.")

def singer():
    name1 = input("좋아하는 가수 1 :")
    name2 = input("좋아하는 가수 2 :")
    name3 = input("좋아하는 가수 3 :")
    print(f"{name1},\n{name2},\n{name3},\n")

#singer()

# n1, n2 = map(int,input().split())
# n1, n2 = n2, n1
# print(n1,n2)

# a = 5
# if a >= 3:
#     print("3이상")
# elif a > 1:
#     print("1초과")
# else:
#     print("1이하")

# n1, n2 = map(int,input().split())
# if n1 > n2:
#     print(n1)
# else:
#     print(n2)

# a = int(input())
# if a >= 70:
#     print("최우수")
# elif a >= 50:
#     print("우수")
# elif a >= 20:
#     print("보통")
# else:
#     print("노력 필요")


# arr = ['b','c','a','f','t','e']
# arr.sort(reverse=True)
# print(arr)
# print(arr[-1])


# score = [55,78,99,38,87]
# score.sort()
# print(score[0],score[-1])

# for i in range(1,10,1):
#     print(i,end=" ")

for i in range(1,101,2):
    print(i,end=" ")
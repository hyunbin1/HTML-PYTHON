a_string = "like this"
a_number = 3
a_float = 3.12
a_boolean = False
#None = 파이썬에만 있음 - 자바스크립트에서는 null과 비슷함.
# 존재하지 않음을 의미
a_none = None

print(type(a_number))


#sequence type = 열거형 타입
#1. list
#2. tuple 

# 1.---- list-----
# 많은 값을 하나의 list에 저장해서 자신이 원하는 자료를 뽑아쓰게 만들자.
# 안의 내용을 ""로 각각 묶어줘야 됨

days = ["Mon","Tue","Wed","Thur","Fri"]
print(days)
# 내용이 존재하는지 찾을때 - "찾을내용" in 리스트 이름 -
print("Mon" in days)
# 3번째 들어있는 내용이 무엇인지 찾을 때
print(days[2])
# 몇개의 내용이 있는지 - list의 길이 알기 - len
print(len(days))

# Mutable = 우리가 값을 바꿀 수 있음
# Immutable = 우리가 값을 바꿀 수 없음 
# list는 Mutable 이다. 
# ex] s.append = 리스트에 내용 추가하기
print(days)
days. append("sat")
print(days)
# s.reverse() = 역방향으로 바꾸기
days.reverse()
print(days)
# s.clear = list 내용 모두 지우기

#2. ----tuple----
#Immutable sequence = tuple = list와 다르게 common sequence operation만 사용 가능하다는 것
# list = []로 감싸고 tuple은 ()로 감싸면 됨

days = ("Mon","Tue","Wed","Thur","Fri")
print(type(days))

# 한 캐릭터를 만들때 = dictionary 만들기 - {} 중괄호 사용 = 모든 type을 넣을 수 있음 - 변수, 글자, boolean 등
# 글자는 ""해주고 숫자는 그냥 사용

nico = {
    "name" : "Nico",
    "Age": "29",
    "korean" : True,
    "fav_food" : ["kimchi","sashimi"],
}

print(nico)

#nico name 만 가져오기
print(nico["name"])

print(nico)
nico["handsome"] = True
print(nico)

# built in function - str(), int(), print(), len(), ... and so on
age = "18"
print(age)
print(type(age))
#age라는 변수를 n_age라는 함수로 만들어주고 이것을 int를 사용해서 
# age라는 변수는 정수라고 정의해줌
n_age = int(age)
print(n_age)
print(type(n_age))


# function 만들기
# funcion을 정의하기 = definition - 들여쓰기 주의하기
# function에 ()하는 것은 ~를 실행한다 라는 뜻 = () = 실행 버튼을 누르기
def say_hello():
    print("hello")
    print("bye")
say_hello()

# function input - (이 안에 input 하고 싶은 내용을 넣어 주면 된다)

def plus(a, b):
    print(a+b)

plus(2,5)
# 이렇게 되면, a,b,c, 등등을 계속 정의 하지 않아도 plus만 사용하면 
# 2개의 연산자를 계산 할 수 있다. 

# 이름 넣어보기
def a(who):
    print("hello", who)

a("김현빈")

# a라는 function을 사용해서 ()안에  원하는 이름만 써주면 앞에서 정의한 print가 사용된다. 

def minus(a,b):
    print(a - b)

minus(4,1)


# default 값을 추가할 수 있움
#인자 1개만 입력해도 실행 가능하다는 의미 - default 값 대신 다른것을 나중에 쓰면 
# default 값 말고 쓴 값이 나옴
def minus (a, b=2):
    print(a-b)
    minus(2)

def say_hello(name="anonymous"):
    print("hello", name)


say_hello()
say_hello("hyun bin")


# ruturn = 어떤 function을 호출할 때 return을 사용하면 funcion이 return으로 치환이 됨
# python에서 function을 ruturn 하는 순간 그 function은 종료가 된다
# 따라서 오직 한번에 하나의 값만 return 할 수 있고 return 후에 사용한 문법들은 인지 X

def p_plus(a, b):
    print(a+b)

def r_plus(a,b):
    return a + b

p_result = p_plus(2,3)
r_result = r_plus(2,3)
# r_result는 앞에서 r_plus가 return을 했기 때문에 2+3은 5로 치환해준다. 
#p_result는 앞에서 return을 안해줬기 때문에 함수 자체는 print 할 수 없다. 
print(p_result, r_result)


# f: 한 문장 안에서 내가 정의한 함수를 사용하고 싶을 때 "" 앞에 f 를 붙이고 정의한 인자에 {}로 해준다
# 굳이 문장을 +로 나눌 필요도 없음
def hi(name, age):
    return f"Hello {name} you are {age} years old"

hello = hi("nico", "12")
print(hello)

# 여러개의 인자가 있을 때 모든 순서를 기억하는것은 어렵다 따라서
# keyword argument 을 사용해주자 - input하는 순서가 바뀌어도 노상관

def hihi(name, age, are_from,fav_food):
    return f"Hello {name} you are {age} you are from {are_from} you like {fav_food}"

hello = hihi(name="nico", fav_food= "kimchi", age = 12, are_from = "seoul")
print(hello)

# Boolean Operations - and, or, not
# x or y = 하나만 충족
# x and y = 둘다 충족
# not x = x가 반드시 false

def age_check(age):
    print(f"you are {age}")
    if age < 18:
        print("you can't drink")
    elif age == 18:
        print("your now to this!")
    elif age >20 and age <25:
        print("you are sill kind of young")
    else:
        print("enjoy your drink")


age_check(23)


# loof => for = 순차적인 작업을 할 때 좋음 = list와 같은 배열들을 순차적으로 가르킨다.
# potato는 Mo된다 Tur 등이 되는 변수이다. 따라서 아무 단어나 들어가도 된다.
# 하지만 days는 꼭 써줘야 된다
days = ("Mon", "Tue", "Wed", "Thu", "Fri")

for potato in days:
    print(potato)

#break = for문 멈추기

for x in days:
    if x in "Wed":
        break
    else:
        print(x)


# import = 어떤 기능들을 가져다가 쓰는 것
# Modules = 그 기능들
# MATE = ceil - 값을 올림해서 반환함
# fabs = 절대값
import math

print(math.ceil(1.2))
print(math.fabs(1.2))


# 모든 module 을 깔기에는 비효율적이다 
# from module import sum,ceil 형식을 사용하여 필요한 기능만 가져오자


from math import fsum, ceil

print (ceil(1.2))
print(fsum([1,2,3,4,5,6,7]))

# import 하면서 이름도 바꿔줄 수 있음
# from math import fsum as wow
# 서로 다른 파일에서도 기능을 가져올 수 있는데
# from 파일명 import 가져올 함수 or 기능
# 형식으로 사용하면 된다. 
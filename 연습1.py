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

#Mutable = 우리가 값을 바꿀 수 있음
#Immutable = 우리가 값을 바꿀 수 없음 
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
#age라는 변수를 n_age라는 함수로 만들어주고 이것을 int를 사용해서 age라는 변수는 정수라고 정의해줌
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
# 이렇게 되면, a,b,c, 등등을 계속 정의 하지 않아도 plus만 사용하면 2개의 연산자를 계산 할 수 있다. 

# 이름 넣어보기
def a(who):
    print("hello", who)

a("김현빈")

# a라는 function을 사용해서 ()안에  원하는 이름만 써주면 앞에서 정의한 print가 사용된다. 

def minus(a,b):
    print(a - b)

minus(4,1)


# default 값을 추가할 수 있움
#인자 1개만 입력해도 실행 가능하다는 의미 - default 값 대신 다른것을 나중에 쓰면 default 값 말고 쓴 값이 나옴
def minus (a, b=2):
    print(a-b)
    minus(2)

def say_hello(name="anonymous"):
    print("hello", name)


say_hello()
say_hello("hyun bin")
    

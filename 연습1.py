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
    "Age": 29,
    "korean" : True,
    "fav_food" : ["kimchi","sashimi"]
}

print(nico)

#nico name 만 가져오기
print(nico["name"])

print(nico)
nico["handsome"] = True
print(nico)



#! django start

#? 부트스트랩 사용 = 오프소스 프레임 워크
# 원하는 파일을 html에 복붙한 후에 부트스트랩 CDN을 html 헤더 부분에 넣어준다.

#? django 시작하는 과정

#! git ignore
# .gitignore 폴더 생성해주기 -> gitignore.io에 들어가서 python,django, visual studio code를 첨가해준다
# 모두 복붙한다음에 14번째줄 media 아래 - venv라고 추가해준다


#! settings.py
# installed app에 app을 입력해준다. page라고만 쳐도 됨('page.apps.PageConfig',)
# 시간 : ko-kr, Asia/Seoul


#! views
def home(request):
    return render(request,'home.html')

#! urls.py
## urlpatterns에 path('',views.home, name="home")이라고 입력해준다. ##

# 1번째:''  = url 주소 만들어주기
# 2번째:view에 있는 home 함수를 가져오는 것. 그냥 url이 views를 부른다음에 home이라는 html을 부른다고 알변 된다.
# 3번째: 이 url 이름을 정의해주기

## 위에 from page import views 첨가해주기= page 앱 중에서 views 내용을 가져온다는것 


#! 각 html간 url 연결시켜주기
# home.html에서 버튼을 누르면 introduce.html에 연결해 주기로하자
#? a href 부분에 introduce.html을 첨가한다고 연결되지 않는다
## 탬플릿 언어를 사용해야됨. {% url 'introduce' %} ##


#!static file 관리

# 1. app 폴더 안에 static 폴더 만들기, css, img 폴더를 static 폴더 안에 첨가
# 2. settings.py(static 설정) 
## static file들이 들어있는 경로 알려주기
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'APP이름', 'static')
 ]

## static file들을 모을 디렉토리 만들어주기
STATIC_ROOT = os.path.join(BASE_DIR,'static')

## 파일 첨가해주기

# 3. static 파일들의 경로와, 담겨져있는 부분을 생성했으니 한곳으로 STATIC 파일 모아줘야 된다.(배포할때 한번만 해줘도 된다.)
## python manage.py collectstatic

# 4. home.html에 파일 경로 추가해주기
#? 우리는 클라이언트와 서버를 왔다갔다 하는 부분을 만드는 것이기 때문에 모두 템플릿 태그를 사용해서 url을 설정해야 된다
##  <a id = "" href="{% url 'home'%"} class=""
    ##<img src = "{% static 'image/sdf.png%}" alt="~png"

## src는 파일 경로를 알려주고 alt는 파일이 없을 경우에 대신 나타나는 창을 의미한다. 



#? tip) 내가 작성한 css를 작용하고 싶다면 헤드 맨 마지막에 적어주기 = 아래서부터 위로 덮어쓰면서 코드를 읽기 때문에

#! MDEIA files

# 1. settings.py
## MEDIA_ROOT = os.path.join(BASE_DIC, 'media')

## MEDIA_URL = '/media/'

# 2. urls.py

## 위에 setting과 static 경로 삽입해주기
## from django.conf import settings
## from django.conf.urls.static import static 

## urlpatterns =[] 끝에
## + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

#첨가해주기 = 사용자들이 올린 스테틱 파일들을 첨가할 수 있게 만들어 주는 것

# 3. HTML에서 사용할 때 = 맨위에 {% load static %} 첨가해서 사용할 수 있게 만들기


#! model을 통해 DB 생성하기!#
# model = 데이터에 접속하고 관리하도록 도와주는 객체

#? model 생성 & 적용
# 모델 생성 -> DB가 알아듣도록 번역 -> 번역한 내용을 DB에 적용

# 1. models.py 
#? 주의] 모델명의 첫 글자는 무조건 대문자!!!

class Designer(models.Model):
    image = models.ImageField(upload_to = 'images/')
    # upload to = 'image/' = settings.py 에서 사용자가 media를 올리면 media 파일로 보낸다고 했는데
    # 파일을 media에 있는 images에 올리겠다고 하는 의미
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 255)
    description = models.TextField()


    # admin 안에서 model의 object의 이름이 아닌 우리가 작성한 name의 값을 반환해서 나타내 달라는 의미
    def __str__(self):
        return self.name


#? models. 다음에 나온 것은 내용 형식을 지정해 준것임

## Image_Field = 이미지가 들어오도록 필드를 만들어 주는것
## CharField = 캐릭터 필드 = 길이가 많이 길지 않을때 사용 = 길이 제한 가능
## TextField = 길이가 긴 곳에 사용된다


# 2. terminal (DB는 django에 있는 model과 다르게 django와 별개이기 때문에 별도로 실행해준다.)
## pip install pillow = djagno에서 이미지를 올리고 작업할때 활용할 수 있게 만듦.

## python manage.py makemigrations ( + app 이름 [특정한 앱만 관리할때 사용])
# db가 알아들을 수 있도록 번역해주는것
## python manage.py migrate ( + app 이름 [특정한 앱만 관리할때 사용])
# 번역된 내용을 db에 알려주는 것

#! ADMIN 관리(생성)하기 !#

# 1. 생성하기 
## python manage.py createsuperuser ##

# 2. admin.py 연결하기(위에)
## from .models import Designer

# 3. 아래에다가 첨가해주기
## admin.site.register(Designer)



#! QuerySet
# 전달받는 모델의 객체 목록

# 1. home.html에 Model의 존재 알려주기
from .models import Designer

# 2. Queryset을 Templates로 보내기

def home(request):
    # Designer.objects,all() == 디자이너에 있는 모든 객체를 보낼 수 있게 만드는 Method이다. 
    designers = Designer.objects.all()
    return render(request, 'home.html', {'designers' : desingers})

#! PK (Primary Key)
# Model을 통해 생성된 객체들을 구분할 수 있는 "고유한" key
# 각각의 글을 분류함

#! Path Convertor
#여러 객체의 url을 "계층적으로" 다룰 수 있도록 도와주는 도구
# urls.py에서 글마다 path를 만들필요가 없게 해줌

## urls.py : path(url 이름/<int:designer)id>/',views.detail,name = "detail")
# 모델 객체 이름/pk를 변수로 설정해줘서 모든 객체 다룰수 있게 해줌

## Template : {% url 'detail' designer.id %}

#! get_object_or_404
#객체를 가져오려 했는데 없을 경우 나타나는 에러
#없는 글을 불러오려고 할때 오류를 제시함
# views.py의 pk변수명과 urls.py의 pk변수명은 같아야함!!
## views.py
 
from django.shortcuts import renter, get_object_or_404

# def template이름(request, urls.py에서 모델 객체 정의한 이름)
def detail(request, designer_id):
    designer = get_object_or_404(Designer,pk = designer_id)
    return render(request, 'detail.html',{'designer' : designer})


# 6강


#! URL Include
## App :
App 폴더 내에 urls.py 생성후 
from django.urls import path 
from . import views 

# 프로젝트에 있는 urls.py에서 url patterns 중 app에 해당되는 urls만 가져오기
Urlpatterns = [~~]

## project/urls.py :
# path옆에 include 추가해주기
from django.urls import path, include

# app이 가져간 urls 자리에 대신 첨가해준다 
urlpatterns = [
    path('url/',include('app이름.urls')),
]
                   
#! template 상속 
#base.html만들어서 중복되는 부분을 다른 html 에서 중복적으로 표기 할 필요 없게 만들어줌

## base.html :
<head>
    <link href-{% block link %}
    
    
    {% endblock %}
</head>

<body>

    {% block content %}

    {% endblock %}
</body>

## home.html
# 맨위에
{% extends 'base.html' %}

#? 새로운 링크 걸어줄때/덮어쓸때
{% block link %}
{% static 'css/home.css' %}
{% endblock%}
#이렇게 치면 base.html head 링크, endblock 사이에 들어가는 것과 같다

#? 새로운 내용 첨가
{% block content %}
~~~
{% endblock %}
# 이렇게 치면 base.html에 블럭 컨텐트, 엔드블록 사이에 들어가는 것과 같다. 



#! 7강

#! CRUD

# 1. CREATE
# 새로운 객체를 생성해 Data를 저장

# 1) 객체 생성
if request.method == "POST":
    post - Designer()

# 2) 입력 Data 저장

post.name = request.POST['name']
post.address = request.POST['address']

# 3) 입력 Data 저장

post.save

# 2. UPDATE
# 정보 수정이 필요한 객체를 찾아 Data를 새롭게 저장

# 1) 객체 탐색
post = get_object_or_404(Designer,pk = designer_id)
if request.method == 'POST':

# 2) 입력 Data 저장
post.name = request.POST['name']
post.address = request.POST['address']


post.save()

# 3. Delete

# 1) 객체 탐색
post = get_object_or_404(Designer,pk = designer_id)

# 2) 객체 삭제
post.delete()

# 3) Home으로 이동
return redirect('home')























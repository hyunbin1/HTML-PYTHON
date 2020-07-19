
#! django start

#? 부트스트랩 사용 = 오프소스 프레임 워크
# 원하는 파일을 html에 복붙한 후에 부트스트랩 CDN을 html 헤더 부분에 넣어준다.

#? django 시작하는 과정

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
## python manage.py collectstatic`

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


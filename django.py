
#! django start

#? 부트스트랩 사용 = 오프소스 프레임 워크
# 원하는 파일을 html에 복붙한 후에 부트스트랩 CDN을 html 헤더 부분에 넣어준다.

#? djangoi 시작하는 과정

# .gitignore 폴더 생성해주기 -> git ignore.io에 들어가서 python,django, visual studio code를 첨가해준다
# 모두 복붙한다음에 14번째줄 media 아래 - venv라고 추가해준다


#! settings.py
# installed app에 app을 입력해준다. page라고만 쳐도 됨('page.apps.PageConfig',)
#ko-kr, Asia/Seoul


#! veiws

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

# 1. app 폴더 안에 static 폴더 만들기, css, img파일 안에 첨가
# 2. settings.py(static 설정) 
## static file들이 들어있는 경로 알려주기
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'APP이름', 'static')
 ]

## static file들을 모을 디렉토리 만들어주기
STATIC_ROOT = os.path.join(BASE_DIR,'static')

# 3. static 파일들의 경로와, 담겨져있는 부분을 생성했으니 한곳으로 STATIC 파일 모아줘야 된다.
## python manage.py collectstatic`









`
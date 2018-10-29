import json

import requests
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import LoginForm, SignupForm, UserProfileForm


def login_view(request):
    # URL: /members/login/
    #  config.urls에서 '/members/'부분을 'members.urls'를 사용하도록 include
    #  members.urls에서 '/login/'부분을 이 view에 연결

    # Template: members/login.html
    #  템플릿의 GET요청시 아래의 LoginForm인스턴스를 사용
    #  POST요청시의 처리는 아직 하지 않음

    # Form: members/forms.py
    #  LoginForm
    #   username, password를 받을 수 있도록 함
    #    password는 widget에 PasswordInput을 사용하기

    context = {}
    if request.method == 'POST':
        # 1. request.POST에 데이터가 옴
        # 2. 온 데이터 중에서 username에 해당하는 값과 password에 해당하는 값을 각각
        #    username, password변수에 할당
        # 3. 사용자 인증을 수행
        #    username/password에 해당하는 사용자가 있는지 확인
        # 4-1. 인증에 성공한다면
        #      세션/쿠키 기반의 로그인과정을 수행, 완료 후 posts:post-list페이지로 redirect
        # 4-2. 인증에 실패한다면
        #      이 페이지에서 인증에 실패했음을 사용자에게 알려줌

        # username, password를 받는 부분을
        # LoginForm을 사용하도록 수정
        #  로그인에 실패했을 경우, Template에 form.non_field_errors를 사용해서
        #  로그인에 실패했다는것을 출력
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            # GET parameter에 'next'가 전달되었다면
            #  해당 키의 값으로 redirect
            next_path = request.GET.get('next')
            if next_path:
                return redirect(next_path)
            return redirect('posts:post-list')
    else:
        form = LoginForm()

    context['form'] = form
    return render(request, 'members/login.html', context)


def logout_view(request):
    # URL: /members/logout/
    # Template: 없음

    # !POST요청일 때만 처리
    # 처리 완료 후 'posts:post-list'로 이동

    # base.html에 있는 'Logout'버튼이 이 view로의 POST요청을 하도록 함
    #  -> form을 구현해야 함
    #      'action'속성의 값을 이 view로
    if request.method == 'POST':
        logout(request)
        return redirect('posts:post-list')


def signup_view(request):
    # render하는 경우
    #  1. POST요청이며 사용자명이 이미 존재할 경우
    #  2. POST요청이며 비밀번호가 같지 않은 경우
    #  3. GET요청인 경우
    # redirect하는 경우
    #  1. POST요청이며 사용자명이 존재하지 않고 비밀번호가 같은 경우

    """
    if request.method가 POST면:
        if 사용자명이 존재하면:
            render1
        if 비밀번호가 같지 않으면:
            render2
        (else, POST면서 사용자명도없고 비밀번호도 같으면):
            redirect
    (else, GET요청이면):
        render
    if request.method가 POST면:
        if 사용자명이 존재하면:
        if 비밀번호가 같지 않으면:
        (else, POST면서 사용자명도없고 비밀번호도 같으면):
            return redirect
    (POST면서 사용자명이 존재하면)
    (POST면서 비밀번호가 같지않으면)
    (POST면서 사용자명이 없고 비밀번호도 같은 경우가 "아니면" -> GET요청도 포함)
    return render
    :param request:
    :return:
    """
    context = {}
    if request.method == 'POST':
        # POST로 전달된 데이터를 확인
        # 올바르다면 User를 생성하고 post-list화면으로 이동
        # (is_valid()가 True면 올바르다고 가정)
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # form이 유효하면 여기서 함수 실행 종료
            return redirect('posts:post-list')
        # form이 유효하지 않을 경우, 데이터가 바인딩된 상태로 if-else구문 아래의 render까지 이동
    else:
        # GET요청시 빈 Form을 생성
        form = SignupForm()

    # GET요청시 또는 POST로 전달된 데이터가 올바르지 않을 경우
    #  signup.html에
    #   빈 Form또는 올바르지 않은 데이터에 대한 정보가
    #   포함된 Form을 전달해서 동적으로 form을 렌더링
    context['form'] = form
    return render(request, 'members/signup.html', context)


@login_required
def profile(request):
    # POST요청시에는 현재 로그인한 유저의 값을
    #  POST요청에 담겨온 값을 사용해 수정
    #  이후 다시 form을 보여줌
    #   f = Form(request.POST,
    #           request.FILES,
    #           instance=<수정할 인스턴스>)
    #   f.save()

    # GET요청시에는 현재 로그인한 유저의 값을 가진
    #  form을 보여줌
    if request.method == 'POST':
        form = UserProfileForm(
            request.POST, request.FILES,
            instance=request.user)
        if form.is_valid():
            form.save()
            # https://docs.djangoproject.com/en/2.1/ref/contrib/messages/
            # is_valid()를 통과하고 인스턴스 수정이 완료되면
            # messages모듈을 사용해서 템플릿에 수정완료 메시지를 표시
            messages.success(request, '프로필 수정이 완료되었습니다')

    form = UserProfileForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'members/profile.html', context)


def facebook_login(request):
    api_get_access_token = 'https://graph.facebook.com/v3.2/oauth/access_token?'
    # URL: /members/facebook-login/
    # URL name: 'members:facebook-login'
    # request.GET에 전달된 'code'값을
    # 그대로 HttpResponse로 출력

    # 페이스북 로그인 버튼의 href안에 있는 'redirect_uri'값을
    # 이 view로 오도록 설정

    # request token
    code = request.GET.get('code')
    # request token을 access token으로 교환
    # 액세스 토큰 교환 엔드포인트에
    #  requests를 사용해서 GET요청
    #  이후 돌아온 response.text를
    #  HttpResponse로 보여주기
    params = {
        'client_id': 187811455470890,
        'redirect_uri':'http://localhost:8000/members/facebook-login/',
        'client_secret': 'f8de96a0fb7df0741128d8237315911c',
        'code': code,
    }
    response = requests.get(api_get_access_token, params)
    # 인수로 전달한 문자열이 'JSON'형식일 것으로 생각
    # json.loads는 전달한 문자열이 JSON형식일 경우, 해당 문자열을 parsing해서 파이썬 Object를 리턴함
    # response_object = json.loads(response.text)
    data = response.json()
    access_token = data['access_token']

    # access_token을 사용해서 사용자 정보를 가져오기
    pass
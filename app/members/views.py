from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from members.forms import LoginForm


def login_view(request):
    # URL: /members/login/
    # config.urls에서 '/members/'부분을 'members.urls'를 사용하도록 include
    # members.urls에서 '/login/'부분을 이 view에 연결

    # Template: members/login.html
    # 템플릿에는 아래의 LoginForm 인스턴스를 사용

    # Form: members/forms.py
    # LoginForm
    # username, password를 받을 수 있도록 함
    # password는 widget에 PasswordInput을 사용하기
    if request.method == 'POST':
        # 1. request.POST에 데이터가 옴
        # 2. 온 데이터 중에서 username에 해당하는 값과 password에 해당하는 값을 각각
        # username, password변수에 할당
        # 3. 사용자 인증을 수행
        #    username/password에 해당하는 사용자가 있는지 확인
        # 4-1. 인증에 성공한다면
        #       세션/쿠키 기반의 로그인과정을 수행, 완료 후 posts:post-list페이지로 redirect
        # 4-2. 인증에 실패한다면
        #       이 페이지에서 인증에 실패했음을 사용자에게 알려줌

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            # 인증 성공시
            return redirect('posts:post-list')

        else:
            # 인증 실패시
            ...
    else:
        form = LoginForm()
        context = {
            'form': form,
        }
        return render(request, 'members/login.html', context)
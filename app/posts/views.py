from django.shortcuts import render

from .models import Post

def post_list(request):
    # 1. Post모델에
    # created_at (생성시간 저장)
    #   auto_now_add=True
    # modified_at (수정시간 저장)
    #   auto_now = True
    # 두 필드를 추가

    # 2. Post모델이 기본적으로 pk내림차순으로 정렬되도록 설정
    #       class Meta:
    #           ordering = ['-pk']

    # 3. 모든 Post 객체에 대한 QuerySet을
    #     render의 context 인수로 전달
    #       context = {'posts': Post.objects.all()}

    # 4. posts/post_list.html을 Template으로 사용
    #     템플릿 에서는 posts값을 순회하며
    #     각 Post의 photo정보를 출력

    # 5. url은 posts.urls모듈을 사용
    #       config.urls에서 해당 모듈을 include
    #       posts.urls.app_name = 'posts'를 사용
    #       include할 URL은 'posts/'
    #       view의 URL은 비워둔다
    #       결과: localhost:8000/posts/로 접근시 이 view가 처리하도록 함
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/post_list.html', context)


def post_create(request):
    # 1. posts/post_create.html 구현
    # form 구현
    #   input[type=file]
    #   button[type=submit]
    
    # 2. /posts/create/ URL에 이 view를 연결
    #         URL명은 'post-create'를 사용
    # 3. render를 적절히 사용해서 해당 템플릿을 return
    # 4. base.html의 nav부분에 '+ Add Post'텍스트를 갖는 a링크 하나 추가,
    #       {% url %} 태그를 사용해서 포스트 생성 으로 링크 걸어주기
    return render(request, 'posts/post_create.html')
# Instagram

인스타그램 만들기

## Installation

### Requirements

#### Python, packages

- Python (3.6)

```
pip install -r requirements.txt
```

#### Secrets

`.secrets/base.json`

```json
{
  "SECRET_KEY": "<Django SECRET_KEY>",
  "FACEBOOK_APP_ID": <Facebook APP ID>,
  "FACEBOOK_APP_SECRET": <Facebook APP Secret>"
}
```

## 모델

- 포스트 (Post)
    - 작성자 (author)
    - 사진 (photo)
    - 댓글 목록
- 포스트 댓글 (Comment)
	- 해당 포스트 (post)
    - 작성자 (author)
    - 내용 (content)
    - 해시태그
    - 멘션
- 해시태그 (HashTag)
    - 태그명 (name)
- 사용자 (User)
    - 사용자명 (username)
    - 프로필 이미지 (img_profile)
    - 이름 (name)
    - 웹사이트 (site)
    - 소개 (introduce)
    
## 화면

- 프로필
	- 내 게시물 목록
	- 내 팔로워 목록
	- 내 팔로잉 목록
- 로그인
- 회원가입
- 포스트 피드 (포스트 리스트)
- 포스트 작성
- 포스트 디테일

## 기능

- 회원가입
- 로그인
- 포스트 작성/삭제
- 팔로우/언팔로우
- 포스트 좋아요/좋아요 취소
- 포스트에 댓글 작성/수정/삭제
	- 댓글 작성 시 해시태그/멘션 추가
- 해시태그 검색
- 프로필 수정
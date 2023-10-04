![image](https://user-images.githubusercontent.com/53895822/190969244-37e2186a-1d99-497a-bbfc-49c79eab7f7c.png)


Pinterest를 모티브로 한 웹페이지입니다.  
Address : http://minirest.site (현재 폐쇄)

## Description
* 게시판 기능 : 글, 댓글(대댓글), 팔로우, 구독, 이미지 업로드, 핀(모음) 등의 기능을 구현했습니다.  
```
    1. 유저 개인의 프로필 및 글을 꾸밀 수 있습니다.
    2. 상단 검색바로 찾고자 하는 글을 검색할 수 있습니다.
    3. 댓글 및 대댓글 기능이 구현되어 있습니다. (댓글 접기 가능)
    4. 유저 및 핀(프로젝트) 팔로우 기능이 구현되어 있습니다. (9/19 팔로우 리스트 보여주는 화면 구현 중)
    5. 본인이 직접 핀(프로젝트)을 생성해서 다른 유저와 함께 공통된 주제의 글을 모아볼 수 있습니다.
    
    * 그 외 추가할 기능들은 미정입니다.
```


**Web Screenshot**
* main
![image](https://user-images.githubusercontent.com/53895822/190965072-e51c11fb-75a8-431c-8d1c-52db7f59f50d.png)
* In Article
![image](https://user-images.githubusercontent.com/53895822/190965026-5000271b-e1f4-4e17-8d21-57ee4a6f22ec.png)


## Built With
minirest는 아래의 스택들로 만들어졌습니다.

* <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
* <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">
* <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
* <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
* <img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white">
* <img src="https://img.shields.io/badge/postgresql-4169E1?style=for-the-badge&logo=postgresql&logoColor=white">
* <img src="https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white">
* <img src="https://img.shields.io/badge/amazonec2-FF9900?style=for-the-badge&logo=amazonec2&logoColor=white">
* <img src="https://img.shields.io/badge/nginx-009639?style=for-the-badge&logo=nginx&logoColor=white">
    
## Directory Structure

<details>
<summary>접기/펼치기</summary>

``` bash
├── README.md
├── accountapp
│   ├── admin.py
│   ├── apps.py
│   ├── decorators.py
│   ├── forms.py
│   ├── migrations
│   ├── models.py
│   ├── templates
│   │   └── accountapp
│   │       ├── create.html
│   │       ├── delete.html
│   │       ├── detail.html
│   │       ├── login.html
│   │       └── update.html
│   ├── urls.py
│   └── views.py
├── articleapp
│   ├── admin.py
│   ├── apps.py
│   ├── decorators.py
│   ├── forms.py
│   ├── migrations
│   ├── models.py
│   ├── templates
│   │   └── articleapp
│   │       ├── create.html
│   │       ├── delete.html
│   │       ├── detail.html
│   │       ├── list.html
│   │       ├── taggit
│   │       │   ├── cloud.html
│   │       │   └── list.html
│   │       └── update.html
│   ├── urls.py
│   └── views.py
├── commentapp
│   ├── admin.py
│   ├── apps.py
│   ├── decorators.py
│   ├── forms.py
│   ├── migrations
│   ├── models.py
│   ├── templates
│   │   └── commentapp
│   │       ├── create.html
│   │       ├── delete.html
│   │       ├── detail.html
│   │       └── update.html
│   ├── urls.py
│   └── views.py
├── config
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── nginx
│       ├── default.conf
│       └── nginx.conf
├── manage.py
├── media
│   ├── article
│   ├── profile
│   └── project
├── minirest
│   ├── asgi.py
│   ├── settings
│   │   ├── base.py
│   │   ├── local.py
│   │   └── prod.py
│   ├── urls.py
│   └── wsgi.py
├── profileapp
│   ├── admin.py
│   ├── apps.py
│   ├── decorators.py
│   ├── forms.py
│   ├── migrations
│   ├── models.py
│   ├── templates
│   │   └── profileapp
│   │       ├── create.html
│   │       └── update.html
│   ├── urls.py
│   └── views.py
├── projectapp
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   ├── models.py
│   ├── templates
│   │   └── projectapp
│   │       ├── create.html
│   │       ├── detail.html
│   │       └── list.html
│   ├── urls.py
│   └── views.py
├── requirements.txt
├── searchapp
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   ├── models.py
│   ├── templates
│   │   └── searchapp
│   │       └── search.html
│   ├── urls.py
│   └── views.py
├── static
│   ├── base.css
│   ├── fonts
│   │   ├── NanumSquareB.otf
│   │   ├── NanumSquareEB.otf
│   │   ├── NanumSquareL.otf
│   │   └── NanumSquareR.otf
│   └── js
│       ├── comment.js
│       └── magicgrid.js
├── subscribeapp
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── templates
│   │   └── subscribeapp
│   │       └── list.html
│   ├── urls.py
│   └── views.py
└── templates
    ├── base.html
    ├── footer.html
    ├── head.html
    ├── header.html
    └── snippets
        ├── card.html
        ├── card_project.html
        ├── card_subs.html
        ├── list_fragment.html
        └── pagination.html
```
</details>

## Reference
- 작정하고 장고! Pinterest 만들기
  > https://github.com/noeul1114/pragmatic

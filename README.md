# Minirest - Django Project

## Description

**Pinterest를 모티브로 한 웹페이지입니다.**
- 게시판 기능 : 글, 댓글(대댓글), 팔로우, 구독, 이미지 업로드, 핀(모음) 등의 기능을 구현했습니다.
- **Website Address : http://minirest.site / https://minirest.site**

<img width="1387" alt="스크린샷 2022-09-19 오후 3 32 04" src="https://user-images.githubusercontent.com/53895822/190961125-45a3a513-2aac-4141-ae3e-c6b9326dc050.png">

## Built With
- minirest는 아래의 기술 스택들로 만들어졌습니다.
* 


## Directory Structure

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

## Reference
- 작정하고 장고! Pinterest 만들기
  > https://github.com/noeul1114/pragmatic

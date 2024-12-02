from django.urls import path
from . import views

urlpatterns=[
    path("",views.home, name="home"),
    path("intro/",views.intro, name="intro"),
    path("register", views.register, name="register"),
    path("login", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("ide/", views.ide, name="ide"),
    path("run_code/", views.run_code, name="run_code"),
    path("keywords/", views.keywords, name="keywords")
]
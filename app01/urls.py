from django.urls import path,re_path
from . import views

urlpatterns=[
    re_path(r'^$',views.index,name='index'),#$表示匹配到$结束
    re_path(r'^user_login/$', views.user_login, name='user_login'),
    re_path(r'^tuichu/$',views.tuichu,name='tuichu'),
    re_path(r'^index/$',views.index,name='index'),
    re_path(r'^question/$',views.question,name='question'),
    re_path(r'^register/$',views.register,name='register'),
    re_path(r'^duanzi/$',views.duanzi,name='duanzi'),
    re_path(r'^add_duanzi/$',views.add_duanzi,name='add_duanzi'),

]
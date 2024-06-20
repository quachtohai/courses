from django.urls import path, include, re_path
from . import views

urlpatterns = [
  path('', views.index ),
  path('welcome/<int:year>/', views.welcome, name ='welcome'),
  path('test/', views.TestView.as_view()) ,
  re_path(r'^welcome2/(?P<year>[0-9]{1,2})/$', views.welcome, name ='welcome'),  
]
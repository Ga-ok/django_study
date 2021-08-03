from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

# /polls/
# 2. 전달받은 path를 통해서 특정 view와 연결해준다. 
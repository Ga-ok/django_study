from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/ 
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

# /polls/
# 2. 전달받은 path를 통해서 특정 view와 연결해준다. 
from django.urls import path

from . import views

app_name = 'pybo'

urlpatterns = [
    # name를 통해 index 별칭부여
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
]
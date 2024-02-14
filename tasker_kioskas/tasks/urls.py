from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('tasks/', views.task_list, name='task_list'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'), 
    path('task/<int:pk>/done/', views.task_done, name='task_done'),
    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/<int:pk>/', views.blog_detail, name='blog_detail'), 
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('tasks/', views.task_list, name='task_list'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'), 
    path('task/<int:pk>/done/', views.task_done, name='task_done'),
    path('project/', views.project_list, name='project_list'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'), 
]
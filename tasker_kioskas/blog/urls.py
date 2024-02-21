from django.urls import path
from . import views

urlpatterns = [  
    path('', views.blog_list, name='blog_list'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'), 
    path('create/', views.BlogCreateView.as_view(), name='blog_create'),
    path('<int:pk>/edit/', views.BlogUpdateView.as_view(), name='blog_update'),
]
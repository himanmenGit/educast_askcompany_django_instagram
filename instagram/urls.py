from django.urls import path
from . import views

app_name = 'instagram'

urlpatterns = [
    path('post_new/', views.post_new, name='post_new'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]

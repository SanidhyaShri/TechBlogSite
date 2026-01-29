from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_post, name='add_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('register/', views.register, name='register'),
    path('like/<int:post_id>/', views.toggle_like, name='toggle_like'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),

]

from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('<str:genre>', views.genre, name='genre'),
    path('edit/<int:post_id>/<str:genre>', views.edit, name='edit'),
    path ('post/<str:genre>', views.post, name='post'),
    
]
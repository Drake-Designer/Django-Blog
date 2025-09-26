from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('profile/', views.profile_page, name='profile'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]

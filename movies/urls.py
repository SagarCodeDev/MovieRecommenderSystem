from django.urls import path
from django.contrib.auth import views as auth_views
from movies import views as user_views
urlpatterns = [
    path('',user_views.Profile,name='profile'),
    path('recommend/',user_views.recommend,name='recommend'),
    path('login/',auth_views.LoginView.as_view(template_name='movies/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='movies/logout.html'),name='logout'),
    path('register/',user_views.register,name='register'),
]
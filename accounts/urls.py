from django.urls import path
from .views import signup_view, profile_view, edit_profile, leaderboard_view,badge_history_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/<str:username>/', profile_view, name='profile'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('leaderboard/', leaderboard_view, name='leaderboard'),
    path('profile/<str:username>/badges/', badge_history_view, name='badge_history'),

]

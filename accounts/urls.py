from  django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    #path('login/', user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    #path('register/', register, name='register'),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='account/password_change_form.html'), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'), name='password_change_done'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='account/password_reset_form.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'), name='password_reset_complete'),
    path('register/',register, name='register'),
    path('', dashboard, name='dashboard'),
    path('edit/', edit, name='edit'),
]
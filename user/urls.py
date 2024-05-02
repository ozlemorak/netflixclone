from django.urls import path
from .views import *


from django.contrib.auth import views as auth_views




urlpatterns = [
    path('register/', userRegister, name="register" ),
    path('login/', userLogin, name="login"),
    path('logout/', userLogout, name="logout"),
    path('hesap/', hesap, name="hesap"),
    path('password_change/', passwordChange, name="password_change"),
    path('account_delete/', accountDelete, name="account_delete"),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset_password_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]


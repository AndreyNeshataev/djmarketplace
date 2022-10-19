from django.urls import path
from .views import RegisterUser, LoginUser, LogoutUser, MyUser, ChangeUser


urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register_url'),
    path('login/', LoginUser.as_view(), name='login_url'),
    path('logout/', LogoutUser.as_view(), name='logout_url'),
    path('account/', MyUser.as_view(), name='account_url'),
    path('<int:pk>/change_user', ChangeUser.as_view(), name='change_user_url'),
]

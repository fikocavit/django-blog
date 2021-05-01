from django.urls import path
from . import views

app_name='App_login'

urlpatterns = [
   path('signup/',views.sign_up,name='signup'),
   path('login/',views.login_user,name='login'),
   path('logout/',views.logout_user,name='logout'),
   path('profile/',views.user_profile,name='profile'),
   path('change-profile/',views.user_change,name='change_profile'),
   path('password/',views.change_password,name='password'),
   path('change-pic/',views.change_pic,name='change-pic'),
]

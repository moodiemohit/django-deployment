from django.urls import path
from userloginapp import views

app_name = 'userloginapp'

# url urlpatterns
urlpatterns= [
    path('',views.register,name='register'),
    path('login/',views.user_login,name='user_login'),
    path('logout/',views.user_logout,name='logout')
]

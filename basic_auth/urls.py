from django.contrib import admin
from django.urls import path
from user.views import login_view,login_api,logout_view,error_api,info_user_view


urlpatterns = [
    #user: 'creator' , password: 'be_happy'
    path('',login_view,name='inicio'),

    path('login/',login_view,name='login2'),
    path('api/login/',login_api,name='login_api'),
    path('logout/',logout_view,name='logout'),

    path('info/',info_user_view,name='info_user'),
    path('admin/', admin.site.urls),

    path('api/error/',error_api,name='error_api'), 
]

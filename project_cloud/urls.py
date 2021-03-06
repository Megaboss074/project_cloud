"""project_cloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import logout
from django.contrib.auth.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^$',views.index,name='test'),
    url(r'^$',views.home,name='home'),
    url('login', views.loginpage, name='login'),
    url('signup', views.signuppage, name='signup'),
    url('bookpage', views.bookpage, name='bookpage'),
    url('reviewpage', views.reviewpage, name='reviewpage'),
    # url('register',views.doregister,name='register'),
    url('profilepage', views.editpage, name='profilepage'),
    url('bookroom', views.bookroom, name='bookroom'),
    url(r'^logout/$', logout, {'next_page': 'home'}, name='logout'),



    # url('login', views.loginpage, {'template_name':'login.html'})

]

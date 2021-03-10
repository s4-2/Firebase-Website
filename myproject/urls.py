"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from todo.views import todoView, addTodo, deleteTodo
from home.views import index

from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('todo/',todoView),
    path('addTodo/', addTodo),
    path('deleteTodo/<int:todo_id>/', deleteTodo),
    path('home/', index),
    path('shop/', include('shop.urls')),
    path('blog/', include('blog.urls')),
    path('mysite/', include('mysite.urls')),
    path('db/', include('db.urls', namespace='db')),

    path('signin/', views.signin),
    path('postsign/', views.postsign),
    path('logout/',views.logout, name="log"),
    path('signup/', views.signup, name="signup"),
    path('postsignup/', views.postsignup, name="postsignup"),
    path('create/',views.create, name="create"),
    path('post_create/', views.post_create)
  

   
    
]


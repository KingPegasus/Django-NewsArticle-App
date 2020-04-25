"""newspaper_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include 

from users.views import SignUpView
from pages.views import HomePageView
from articles.views import (
	ArticleListView,
	ArticleUpdateView,
	ArticleDetailView,
	ArticleDeleteView,
	ArticleCreateView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),


    #From users
    path('users/signup/', SignUpView.as_view(), name='signup'),

    #From pages
    path('', HomePageView.as_view(), name='home'),

    #From articles
    path('articles/', ArticleListView.as_view(), name='article_list'),
    path('articles/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
	path('articles/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
	path('articles/new/', ArticleCreateView.as_view(), name='article_new'),

]

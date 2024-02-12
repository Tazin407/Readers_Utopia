"""
URL configuration for Readers_Utopia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from core import views as core
from users import views as user
from books import views as book
from transactions import views as trans


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', book.home, name='home'),
    path('accounts/profile/', book.home, name='home'),
    path('user_signup/', user.SignUp.as_view(), name='user_signup'),
    path('user_login/', user.Login.as_view(), name='user_login'),
    path('user_Logout/', user.Logout, name='user_logout'),
    path('sort_category/<int:id>', book.sort_cat, name='sort_category'),
    path('details/<int:id>', book.Detail.as_view(), name='details'),
    path('deposit', trans.deposit, name='diposit'),
    path('borrow/<int:id>',trans.borrow, name='borrow'),
    path('profile/',trans.Show_Borrow_report.as_view(), name='profile'),
    path('return/<int:id>',trans.return_book, name='return'),
]

if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

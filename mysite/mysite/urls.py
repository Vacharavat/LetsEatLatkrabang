"""mysite URL Configuration

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
from django.urls import path,include
from authen import views
from django.contrib.auth import views as auth_views
from webpage import views as views2
from management import views as views3
from myprofile import views as views4
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.mylogin, name='login'),
    path('logout/', views.my_logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views4.profile, name='Profile'),
    path('', views2.index, name='index'),
    path('<int:type_id>', views2.index_type, name='index_type'),
    path('restaurant_delete/<int:restaurant_id>', views3.restaurant_delete, name='restaurant_delete'),
    path('management/', views3.Management, name='Management'),
    path('add_restaurant/', views3.Add_Restaurant, name='Add_Restaurant'),
    path('restaurant_edit/<int:restaurant_id>', views3.restaurant_edit, name='Restaurant_edit'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

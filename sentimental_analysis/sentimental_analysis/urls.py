"""sentimental_analysis URL Configuration

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
from django.urls import path
import realworld.views
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('home', realworld.views.analysis, name='analysis'),
    path('input', realworld.views.input, name='input'),
    path('productanalysis', realworld.views.productanalysis,name='product analysis'),
    path('textanalysis', realworld.views.textanalysis, name='text analysis'),
    path('audioanalysis', realworld.views.audioanalysis, name='audio analysis'),
    path('home',realworld.views.analysis,name='analysis'),
    path('input',realworld.views.input, name='input'),
    path('productanalysis',realworld.views.productanalysis, name='product analysis'),
    path('textanalysis',realworld.views.textanalysis, name='text analysis'),
    path('audioanalysis',realworld.views.audioanalysis, name='audio analysis'),
    path('ytanalysis',realworld.views.ytanalysis, name='youtube comments analysis'),
    path('signup', realworld.views.signup, name='signup'),
    path('signin', realworld.views.signin, name='signin'),
    path('', realworld.views.signup, name='signup'),
    path('ytanalysis', realworld.views.ytanalysis,name='youtube comments analysis'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from home.views import *
from vege.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('success_page/' , success_page , name='success_page'),
    path('index/', home, name='home'),
    path('about/' , about , name='about'),
    path('contact/' , contact , name='contact'),
    path('admin/', admin.site.urls),
    path('' , recepies  , name='recipies' ),
    path('update_rec/<id>/' , update_rec , name='update_rec'),
    path('delete-receipe/<id>/' , delete_receipe , name='delete_receipe'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()
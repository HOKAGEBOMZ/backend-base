"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from core.views import index, signup, magic
from blog.views import blog
from django.conf.urls.static import static
from django.conf import settings
from ultradoom.views import ultradoom
from ultradoom.views import upload


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('signup/', signup),
    path('magic/', magic),
    path('blog/', blog),
    path('ultradoom/', ultradoom),
    path('upload/', upload),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
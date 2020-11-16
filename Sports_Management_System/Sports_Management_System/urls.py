"""Sports_Management_System URL Configuration

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
from django.urls import path,include
# for login logout signup and all following view is imported from django lib.
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    path('',include('Home_Page.urls')),
    path('register/',include('Home_Page.urls')),
    path('admin/', admin.site.urls),
    path('Events/', include('Events.urls')),
    path('Feedback/', include('Feedback.urls')),
    path('Resource_Management/', include('Resource_Management.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# from core.views import front
from core.views import UserAvatarUpload
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-post/', include('post.urls')),
    path('api-core/', include('core.urls')),
    # path('api-prediction/', include('core.urls')),
    path('api-predict/', include('core.urls')),
    path("", TemplateView.as_view(template_name="index.html")),
    path("api/auth-token/", obtain_auth_token, name="rest_auth_token"),
    path("api/user-avatar/", UserAvatarUpload.as_view(), name="rest_user_avatar_upload"),
]

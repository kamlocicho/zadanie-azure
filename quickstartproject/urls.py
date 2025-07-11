"""quickstartproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path
from ninja import NinjaAPI
from api.api import router as api_router
from authentication_system.api import router as auth_router

api = NinjaAPI()
api.add_router("authentication/", auth_router)
api.add_router("", api_router)

urlpatterns = [
    path('', include('hello_azure.urls')),
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]

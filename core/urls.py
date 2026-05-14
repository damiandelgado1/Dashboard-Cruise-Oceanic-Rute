from django.contrib import admin
from django.urls import path
from .views import dashboard_home


app_name = "core"

urlpatterns = [
    path('home/', dashboard_home, name="home"),
    path('admin/', admin.site.urls),
]
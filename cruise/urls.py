from django.contrib import admin
from django.urls import path

app_name = "cruise"

urlpatterns = [
    path('admin/', admin.site.urls),
]
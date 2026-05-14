from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('cruise/', include("cruise.urls", namespace="cruise")),
    path('rooms/', include("rooms.urls", namespace="rooms")),
    path('admin/', admin.site.urls),
]
from django.contrib import admin
from django.urls import path, include
from .views import home


urlpatterns = [
    path('', home, name="home"),
    path('core/', include("core.urls", namespace="core")),
    path('cruise/', include("cruise.urls", namespace="cruise")),
    path('room/', include("room.urls", namespace="room")),
    path('admin/', admin.site.urls),
]
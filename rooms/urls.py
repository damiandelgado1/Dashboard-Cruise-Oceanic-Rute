from django.contrib import admin
from django.urls import path
from .views import ListRoom, DetailRoom, CreateRoom, ModifyRoom, DeleteRoom


app_name = "rooms"

urlpatterns = [
    path('list/', ListRoom.as_view(), name="room_list"),
    path('detail/<int:pk>/', DetailRoom.as_view(), name="room_detail"),
    path('create/', CreateRoom.as_view(), name="create_room"),
    path('modify/<int:pk>/', ModifyRoom.as_view(), name="modify_room"),
    path('delete/<int:pk>/', DeleteRoom.as_view(), name="delete_room"),
    path('admin/', admin.site.urls),
]
from django.contrib import admin
from django.urls import path
from .views import ListCruise, DetailCruise, CreateCruise, ModifyCruise, DeleteCruise


app_name = "cruise"

urlpatterns = [
    path('list/', ListCruise.as_view(), name="cruise_list"),
    path('detail/<int:pk>/', DetailCruise.as_view(), name="cruise_detail"),
    path('create/', CreateCruise.as_view(), name="create_cruise"),
    path('modify/<int:pk>/', ModifyCruise.as_view(), name="modify_cruise"),
    path('delete/<int:pk>/', DeleteCruise.as_view(), name="delete_cruise"),
    path('admin/', admin.site.urls),
]
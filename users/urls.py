from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    # path("users/<int:pk>/detail", views.getRoutes, name="user_detail"),
    #         path("", views.UserListView.as_view(), name="all"),
    #     path("users/create/", views.UserCreateView.as_view(), name="user_create"),
    #     path("users/<int:pk>/update/", views.UserUpdateView.as_view(), name="user_update"),
    #     path("users/<int:pk>/delete/", views.UserDeleteView.as_view(), name="user_delete"),
]

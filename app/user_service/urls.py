""""
URL mappings for user API.
"""

from django.urls import path

from user_service import views

app_name = "user_service"

urlpatterns = [
    path("create/", views.CreateUserView.as_view(), name="create"),
    path("auth/", views.CreateTokenView.as_view(), name="auth"),
    path("", views.ManageUserView.as_view(), name="user")
]

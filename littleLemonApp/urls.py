from django.urls import path
from . import views

urlpatterns = [
    path(
        "groups/manager/users",
        views.GroupViewSet.as_view(
            {"get": "list", "post": "create", "delete": "destroy"}
        ),
    ),
]
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path(
        "logout/",
        LogoutView.as_view(next_page="login"),
        name="logout"
    ),
    path("tasks/create/", views.task_create, name="task_create"),
    path("tasks/<int:pk>/edit/", views.task_edit, name="task_edit"),
    path("tasks/<int:pk>/delete/", views.task_delete, name="task_delete"),
]
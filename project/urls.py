from django.urls import include, path

from . import views


app_name = "project"

#url for adding new repo to the project
urlpatterns = [
    path('repository/', views.add_repository, name="addRepository"),
]

from django.urls import include, path

from . import views

#define app name 
app_name = "user"

#url's for the web app
urlpatterns = [
	path('', views.homepage, name="homepage"),
	path('login/', views.login_request, name="login"),
	path('register/', views.register_request, name="register"),
	path('logout/', views.logout_request, name="logout"),
	path('repository/', views.add_repository, name='addRepository')
]

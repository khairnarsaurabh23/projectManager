from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, ValidationError
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from . forms  import register
from . models import User
from project import views as pviews


#protected route using decorator
@login_required(login_url='login/')
def homepage(request):
	return render(request,"user/home.html")

def register_request(request):
	#specify a POST request
	if request.method == "POST":
		form = register(request.POST)
		if form.is_valid():
			#save user
			user = form.save()
			user.save()
			username = form.cleaned_data.get('username')
			login(request, user)
			messages.info(request, f"You are now logged in as: {username}")

			return render( request, 'user/root.html')

		else:
			try:
				validate_email( email )
			except :
				messages.error(request,"This email has alredy been taken, try another.")
			redirect('user:register')

	form = register()
	return render(request,
				"user/register.html",
				context={'form':form})


def logout_request(request):
	logout(request)
	messages.info(request, f"Logged out successfully")
	return redirect('user:login')

#handle login request
def login_request(request):
	#specify the POST request
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(request, username='username', password='password')
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as: {username}")
				#redirect user to the homepage
				return redirect("user:homepage")
			else:
				messages.error(request, f"Invalid username or passwword")
				return redirect("user:login_request")
		else:
			messages.error(request, f"Invalid username or passord")
			return HttpResponse("user:login_request")

	#load the AuthenticationForm 
	form = AuthenticationForm()
	return render(request,
				  "user/login.html",
				  {"form":form})

#add a new repository
def add_repository(request):
	return redirect('project:addRepository')

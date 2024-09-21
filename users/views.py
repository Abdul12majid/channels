from django.shortcuts import render, HttpResponse, redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password1']
		check_username = User.objects.filter(username=username)
		if check_username.exists():
			user = authenticate(request, username=username, password=password)
			if User is not None:
				login(request, user)
				return redirect('index')
			else:
				print("error loggin in")
				return redirect('index')
		return redirect('register')

	return render(request, 'login.html')


def profile(request, pk):
	user = request.user
	profile = Profile.objects.get(profile_owner__username=pk)
	pk = 1
	context = {
		"user":user,
		"profile":profile,
	}
	return render(request, 'profile.html', context)


def verify_log_details(request):
	username = request.POST.get('username')
	if User.objects.filter(username=username).exists():
		return HttpResponse("<p class='success'>You can login</p>")
	else:
		return HttpResponse("<p class='error'>Username not found</p>")

def verify_username(request):
	username = request.POST.get('username')
	if len(username) < 5:
		return HttpResponse("<p class='error'><b>Username too short.</b></p>")
	elif User.objects.filter(username=username).exists():
		return HttpResponse("<p class='error'><b>Username taken, pick another.</b></p>")
	elif password1 != password2:
		return HttpResponse("<p class='error'><b>Password does not match</b></p>")
	else:
		return HttpResponse("<p class='success'><b>Username available.</b></p>")

def verify_password(request):
	password1 = request.POST.get('password1')
	password2 = request.POST.get('password2')
	if len(password1) < 4:
		return HttpResponse("<p class='error'><b>Password too short.</b></p>")
	elif password2 != password1:
		return HttpResponse("<p class='error'><b>Password does not match !!!</b></p>")



def register(request):
	return render(request, 'register.html')


from django.shortcuts import render
from .models import Profile

# Create your views here.

def login_user(request):
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

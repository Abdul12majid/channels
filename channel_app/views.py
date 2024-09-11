from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import *
from users.models import Profile
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
	user = request.user
	#chat_group = ChatGroup.objects.get(group_name="")
	chat_group = get_object_or_404(ChatGroup, group_name="public-chat")
	chat_messages = chat_group.chat_messages.all()[:30]
	context = {
		'chat_messages':chat_messages,
		'user':user,
	}
	return render(request, 'index.html', context)


#{% url 'profile' message.author.username %}
def profile(request, pk):
	user = request.user
	get_profile = Profile.objects.get(username=pk)
	pk = get_profile.username
	return HttpResponse('hm')


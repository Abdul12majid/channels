from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import *
from users.models import Profile
from django.contrib.auth.decorators import login_required
from .forms import ChatMessageForm

# Create your views here. 

@login_required
def index(request):
	user = request.user
	#chat_group = ChatGroup.objects.get(group_name="")
	chat_group = get_object_or_404(ChatGroup, group_name="public-chat")
	chat_messages = chat_group.chat_messages.all()[:30]
	form = ChatMessageForm()
	if request.htmx:
		form = ChatMessageForm(request.POST)
		if form.is_valid():
			message = form.save(commit=False)
			message.author = user
			message.group = chat_group
			message.save()
			context = {
				'message':message,
				'user':user,
			}
			return render(request, 'htmx_folder/chat_message_p.html', context)

	context = {
		'chat_messages':chat_messages,
		'user':user,
		'form':form,
	}
	return render(request, 'index.html', context)


#{% url 'profile' message.author.username %}
def profile(request, pk):
	user = request.user
	get_profile = Profile.objects.get(username=pk)
	pk = get_profile.username
	return HttpResponse('hm')


from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import *
from users.models import Profile
from django.contrib.auth.decorators import login_required
from .forms import ChatMessageForm
from django.http import Http404

# Create your views here. 

@login_required
def index(request, chatroom_name='public-chat'):
	user = request.user
	#chat_group = ChatGroup.objects.get(group_name="")
	chat_group = get_object_or_404(ChatGroup, group_name=chatroom_name)
	chat_messages = chat_group.chat_messages.all()[:30]
	form = ChatMessageForm()

	other_user = None
	if chat_group.is_private:
		if request.user not in chat_group.members.all():
			raise Http404
		for member in chat_group.members.all():
			if member != request.user:
				other_user = member
				break

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
		'other_user': other_user,
		'chatroom_name': chatroom_name,
	}
	return render(request, 'index.html', context)


def get_or_create_chatroom(request, username):
	if request.user.username == username:
		return redirect('index')

	other_user = User.objects.get(username = username)
	my_chatrooms = request.user.chat_groups.filter(is_private=True)

	if my_chatrooms.exists():
		for chatroom in my_chatrooms:
			if other_user in chatroom.members.all():
				chatroom = chatroom
				break
			else:
				chatroom = ChatGroup.objects.create(is_private=True)
				chatroom.members.add(other_user, request.user)
	else:
		chatroom = ChatGroup.objects.create(is_private=True)
		chatroom.members.add(other_user, request.user)

	return redirect('chatroom', chatroom.group_name)

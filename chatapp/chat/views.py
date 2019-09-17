from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


def home(request):
	title = "Django_Chat"
	return render(request,'main.html',{"title":title})

def chat(request):
	if request.method != "POST":
		return HttpResponseRedirect(reverse('index'))
	else:
		title = "Chat_Room"
		username = request.POST.get('username')
		return render(request,'chat.html',{"title":title,"username":username})
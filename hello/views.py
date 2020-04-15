from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def my_view(request):
	return render(request, 'hello.html')
	#return HttpResponse('Hello, dear friend!')

def go_todo(request):
    return HttpResponseRedirect('/todo/')
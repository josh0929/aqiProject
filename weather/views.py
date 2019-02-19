from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def Home(request):
	context = ''
	template = loader.get_template('weather/index.html')
	return render(request, 'weather/index.html', context)

def About(request):
	return HttpResponse("About Page")



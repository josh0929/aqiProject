from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import fileIO
import requests

def Home(request):
	#AIRVisual API request
	av_site = "https://api.airvisual.com/v2/nearest_city?key="
	#api_key = fileIO.read_from_file("api_key.json")
	#my_api_key = api_key["api_key"]
	my_api_key = 
	url = av_site + my_api_key
	air_data = requests.get(url).json()

	#Data
	context = {
		'tp'   : air_data["data"]["current"]["weather"]["tp"],
		'long' : air_data["data"]["location"]["coordinates"][0],
		'lat' : air_data["data"]["location"]["coordinates"][1],
	}

	#Loas data
	template = loader.get_template('weather/index.html')
	return render(request, 'weather/index.html', context)

def About(request):
	return HttpResponse("About Page")

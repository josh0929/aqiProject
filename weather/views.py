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
	my_api_key = "6hqhr8n2SW9PXHtLh"
	url = av_site + my_api_key
	air_data = requests.get(url).json()

	#Celcius to fahrenheit conversion
	celcius = air_data["data"]["current"]["weather"]["tp"]
	farenheit = ((celcius * 9)/5) + 32

	#img string
	img = air_data["data"]["current"]["weather"]["ic"]
	img_str = 'img/' + img + '.png'

	#Data
	context = {
		'tpc'     : air_data["data"]["current"]["weather"]["tp"],
		'tpf'	  : farenheit,
		'long'    : air_data["data"]["location"]["coordinates"][0],
		'lat'     : air_data["data"]["location"]["coordinates"][1],
		'city'    : air_data["data"]["city"],
		'state'	  : air_data["data"]["state"],
		'ic'      : img_str,

		'hu'      : air_data["data"]["current"]["weather"]["hu"],
		'pr'      : air_data["data"]["current"]["weather"]["pr"],
		'wd'	  : air_data["data"]["current"]["weather"]["wd"],
		'ws'      : air_data["data"]["current"]["weather"]["ws"],
		'ts'      : air_data["data"]["current"]["pollution"]["ts"],
		'aqius'	  : air_data["data"]["current"]["pollution"]["aqius"],
		'mainus'  : air_data["data"]["current"]["pollution"]["mainus"],
		'aqicn'   : air_data["data"]["current"]["pollution"]["aqicn"],
		'maincn'  : air_data["data"]["current"]["pollution"]["maincn"],
	}

	#Loas data
	template = loader.get_template('weather/index.html')
	return render(request, 'weather/index.html', context)

def About(request):
	return HttpResponse("About Page")

from django.shortcuts import render

import csv
import json
# from urllib.request import urlopen
import urllib.request
import requests
from django.http import HttpResponse
from magic.models import Extension,Carte

def index(request):
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    url = "https://mtgjson.com/json/SS2.json"
    headers = {'User-Agent': user_agent, }
    request = urllib.request.Request(url, None, headers)  # The assembled request
    response = urllib.request.urlopen(request)
    source = response.read()  # The data u need
    data = json.loads(source)
    del data['cards']
    del data['meta']
    del data['tokens']
    del data['translations']
    del data['tcgplayerGroupId']
    extension = Extension(**data)
    print("abc",extension)
    extension.save()
    #carte = Carte({'name':"toto",'idPCA':"machin"})
    #carte.save()
    # for cle in data.keys():
    #     print(cle)
    #     print("-------------------------------------------------------------")
    #
    # for valeur in data.values():
    #     print(valeur)
    #     print("=============================================================")
    # for cle, valeur in data.items():
    #     print(cle, valeur)
    #     print("*************************************************************")
    #return HttpResponse(data['name'])
    return HttpResponse("Hello, world. You're at the magic index.")

    def home0_view(request, *args, **kwargs):
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
        writer = csv.writer(response)
        writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
        writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])
        return response


def home1_view(request, *args, **kwargs):
    # get JSON string data from CityBike NYC using web requests library
    json_response = requests.get("https://mtgjson.com/json/SS2.json")
    # check type of json_response object
    print(type(json_response.text))
    # load data in loads() function of json library
    bike_dict = json.loads(json_response.text)
    # check type of news_dict
    print(type(bike_dict))
    # now get stationBeanList key data from dict
    print(bike_dict['stationBeanList'][0])
    return HttpResponse(bike_dict['stationBeanList'][0])


def home_view(request):
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    url = "https://mtgjson.com/json/SS2.json"
    headers = {'User-Agent': user_agent, }
    request = urllib.request.Request(url, None, headers)  # The assembled request
    response = urllib.request.urlopen(request)
    source = response.read()  # The data u need
    data = json.loads(source)
    extension = Extension(data)
    extension.save()
    # for cle in data.keys():
    #     print(cle)
    #     print("-------------------------------------------------------------")
    #
    # for valeur in data.values():
    #     print(valeur)
    #     print("=============================================================")
    # for cle, valeur in data.items():
    #     print(cle, valeur)
    #     print("*************************************************************")
    return HttpResponse(data['name'])


def contact_view(request, *args, **kwargs):
    return HttpResponse("<h1> Page de contacte </h1>")


def about_view(request, *args, **kwargs):
    return HttpResponse("<h1> A propos de nous </h1>")


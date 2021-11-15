from django.http import response
from django.shortcuts import render
import os
import requests
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated


SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))
# Create your views here.

def ok(request):
    return render(request, 'ok.htm')

# @api_view

def home(request):
    temp = request
    print(temp, "+++")
    temp = str(temp)

    if temp.find("=")!=-1:
        temp = temp[temp.index("=")+1:len(temp)-2]
        response = requests.get('https://anapioficeandfire.com/api/books/?name='+temp).json()
        
    else:
        print("========================")
    
        response = requests.get('https://anapioficeandfire.com/api/books/').json()

    for i in range(len(response)):
        del response[i]['url']
        del response[i]['characters']
        del response[i]['mediaType']
        del response[i]['povCharacters']            


    return render(request, 'home.html', {'response':response})



from tkinter import OFF, ON
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse( '''<a href="https://www.youtube.com/">Youtube</a>''' )

def index(request):
    dic={
        "name":"Harshit",
        "place":"Dehradun"
    }
    return render(request, 'index.html' )

def removepunc(request):
    # if(rempuc ==ON)
    errored = request.POST.get('text')
    cheak1 = request.POST.get('rempuc','off')
    cheak2 = request.POST.get('caps','off')
    cheak3 = request.POST.get('newlinerem','off')
    cheak4 = request.POST.get('extraspace','off')

    analysed = errored
    if cheak1 == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        
        new_text=""
        for char in analysed:
            if char not in punctuations:
                new_text = new_text + char
        analysed=new_text
        

    if  cheak2 == "on" :
        capitalized_text=""
        for char in analysed:
            capitalized_text=capitalized_text + char.upper()

        analysed=capitalized_text; 

    if  cheak3 == "on" :
        new_text=""
        for char in analysed:
            if char != "\n" and char!="\r":
                new_text=new_text + char 

        analysed=new_text; 

    if  cheak4 == "on" :
        new_text=""
        for index,char in enumerate(analysed):
            if not (analysed[index]==" " and analysed[index-1]==" " ):
                new_text=new_text + char 

        analysed=new_text; 

          





    if cheak1=="off" and cheak2=="off" and cheak3=="off" and cheak3=="off"  :
        return HttpResponse("Error")

    else :
        dic={
                'same':errored,
                'correct':analysed
                }
        return render (request,'analyse.html',dic) 
    

def capfirst(request):
    return HttpResponse("capitalize first")
    ''' <br> <a href="http://127.0.0.1:8000/">BACK</a> '''


def newlinerem(request):
    return HttpResponse("newlinerem")
def spacerem(request):
    return HttpResponse("spacerem")
def charcount(request):
    return HttpResponse("charcount")



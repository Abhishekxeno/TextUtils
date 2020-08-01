# I have created this file -Abhi
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):

    #taking the text values
    djtext = request.POST.get('text','default')

    #taking the checkbox values
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcapital','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')

    #to check which checkbox is on
    if (removepunc)=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed= analyzed + char

        params= {'purpose':'Removed Punctuation' , 'analyzed_text': analyzed}
        djtext=analyzed

    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Upper Case', 'analyzed_text': analyzed}
        djtext=analyzed

    if (extraspaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] ==" "):
                analyzed=analyzed+char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}

    if(removepunc!="on" and fullcaps!="on" and  extraspaceremover!="on"):
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)

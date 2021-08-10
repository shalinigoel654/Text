
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render (request,'index.html')


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc','off')
    uppercase=request.POST.get('uppercase','off')
    newline = request.POST.get('newline', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)
    if(uppercase=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Uppercase Character', 'analyzed_text': analyzed}
        djtext=analyzed

    if(newline=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Uppercase Character', 'analyzed_text': analyzed}
        djtext=analyzed

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        djtext=analyzed
    if(uppercase!="on" and newline!="on" and extraspaceremover != "on" and removepunc != "on"):
        return HttpResponse("Please select any operation and try again ")

        # Analyze the text


    return render(request, 'analyze.html', params)


# I have Created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # params = {'name' : 'Shivam', 'place' : 'Delhi'}
    # return render(request, 'index.html', params)
     return render(request, 'index.html')

    # return HttpResponse('''<h1>Hello, Shivam</h1> <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> Django Course </a>
    # <a href="about"> about </a>
    # <a href="remove"> remove </a>
    # <a href="capatilize"> capatilize </a>
    # ''' )

def about(request):
    return HttpResponse("About Shivam")

def removeline(request):
    return HttpResponse("Remove first line")

# def capatilize(request):
     # Get the text from textarea
#     djtext = request.GET.get("text", 'default')
#     return HttpResponse("Captilize first line")   

def analyze(request):
    #  Get the text from textarea
    djtext = request.POST.get("text", 'default')

    removepunc = request.POST.get('removepunc', 'off')     
    spaceremover = request.POST.get('spaceremover', 'off')    
    fullcaps = request.POST.get('fullcaps', 'off')     
    newlineremover = request.POST.get('newlineremover', 'off')     
    countchar = request.POST.get('countchar', 'off')     


    # check values of checkbox
    if removepunc == "on":
         punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
         analyzed = " "
         for char in djtext:
             if char not in punctuations:
                 analyzed = analyzed + char
         params = {'purpose':'Remove Punctuations', 'analyzed_text' : analyzed }
         djtext = analyzed  
         return render(request, 'analyze.html', params)

    if (spaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] =="" and djtext[index+1] == " "):
                analyzed =  analyzed + char 
    
        params = {'purpose':'Remove Extra Space', 'analyzed_text' : analyzed }
        return render(request, 'analyze.html', params)

    elif fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
    
        params = {'purpose':'Capatialize the text', 'analyzed_text' : analyzed }
        return render(request, 'analyze.html', params)    
    
    
    elif newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if djtext != "/n" and char != "/r":
                analyzed = analyzed + char
        
        params = {'purpose':'Remove the New Lines', 'analyzed_text' : analyzed }
        return render(request, 'analyze.html', params)    

    elif countchar == "on":
        analyzed = len(djtext)

        # for char in djtext:
        #     analyzed = analyzed + len(char)
              
        params = {'purpose':'Count the Characters', 'analyzed_text' : analyzed }
        return render(request, 'analyze.html', params)    

    else: 
        return HttpResponse("Error")


from django.shortcuts import render

# Create your views here.
def likedlecture(request):
    return render(request, 'likedlecture.html')

def mytype(request):
    return render(request, 'mytype.html')

def selectkeyword(request):
    return render(request, 'selectkeyword.html')


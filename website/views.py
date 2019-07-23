from django.shortcuts import render

# Create your views here.
def index(request):
    
    return render(request, 'website/index.html')
    
def pl(request):
    
    return render(request, 'website/index.html')
from django.shortcuts import render

# Create your views here.

def index(request):
    print('user acess index')
    return render(request, 'myPages/index.html')

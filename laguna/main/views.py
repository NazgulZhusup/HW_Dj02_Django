from django.shortcuts import render

# Create your views here.
def index(request):
     data = {
      'caption':'Laguna City'
      }
     return render(request, 'main/index.html', data)

def first(request):
      return render(request, 'main/first.html')


def second(request):
    return render(request, 'main/second.html')


def third(request):
    return render(request, 'main/third.html')


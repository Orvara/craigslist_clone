from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'base.html')

def my_app(request):
    return render(request,'base.html')

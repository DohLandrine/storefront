from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def sayHello(request):
    return render(request, 'hello.html', {'name' : 'Doh'})

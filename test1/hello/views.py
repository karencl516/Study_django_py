from django.http import HttpResponse
from django.shortcuts import render

def coin(request):
    num = 0
    context = {'num': num}
    return  render(request, 'hello/coin.html',context)



def hello(request):
    return render(request, 'hello/index.html')

def greetings(request, name):
    context = {'name':name}
    return render(request, 'hello/greetings.html',context)







# Create your views here.
# def vader(request):
#     return HttpResponse("Hello,Darth Vader")
#
# def starwars(request):
#     return HttpResponse("Star Wars")
from django.shortcuts import render
from django.http import HttpResponse

def cart(request):
    cartdetail ={'Name':['umar','abubakar','junaid'],
              'product':['gorrrsary','toys','medicense'],
              'order':['No.3','No.2','No.3']}
    return render(request,'cart.html',cartdetail)
# Create your views here.

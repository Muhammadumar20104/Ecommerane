from django.shortcuts import render
from django.http import HttpResponse

def product(request):
    productdetail ={'productdetail':[{'Name':'Umar','price':'2000','discription':'toys','tax':'5'},{'Name':'Abubakar','price':'3000','discription':'gORROSRY','tax':'6'},{'Name':'junaid','price':'4000','discription':'gift','tax':'7'}]}
    return render(request,'product.html',productdetail)
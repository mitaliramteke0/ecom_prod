from django.shortcuts import render
from product.models import Product
# Create your views here.

def get_by_id(request,id):
    prod=Product.objects.get(pk=id)
    return render(request,'home.html',{"consumers":[prod]})



def get_by_all(request):
    prod=Product.objects.all()
    return render(request,'home.html',{"consumers":prod})

def get_by_filter(request, fil):
        prod = Product.objects.filter(warranty=fil).all()
        return render(request, 'home.html', {"consumers": [prod]})
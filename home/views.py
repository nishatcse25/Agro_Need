from django.shortcuts import render
from products.models import Products

# Create your views here.
def showhomeProduct(request):
    product = Products.getAllProducts()
    all_data = {}
    all_data['allProducts'] = product
    return render(request,'home/home.html', all_data)

def aboutUs(request):
    return render(request,"home/aboutus.html")
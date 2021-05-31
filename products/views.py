from django.shortcuts import render,redirect
from django.contrib import messages
from django.db.models import Q
from .models import *
from seller.models import *
from customer.models import *

def addProduct(request):
    if request.method == "POST":
        productname = request.POST["productname"]
        productprice = request.POST["productprice"]
        productdetails = request.POST["productdetails"]

        x = TemporaryS.objects.get(id=1)
        seller = Seller.objects.get(Q(sellerName=x.sellerName) & Q(sellerPassword=x.sellerPassword))

        add = Products(sellerId=seller.id,productName=productname,productPrice=productprice,productDetails=productdetails)

        add.save()
        messages.info(request,"Product Added")
        return redirect("addproduct")

    return render(request,'products/addproduct.html')


def showProduct(request):
    if request.method == "GET":

        products = Products.objects.filter()
        context = {'products': products}

        return render(request, 'products/showproductlist.html', context)

    else:
        productid = request.POST["productid"]
        productname = request.POST["productname"]

        if productid == "":
            products = Products.objects.filter(productName=productname)
            context = {'products': products}

            return render(request, 'products/showproductlist.html', context)

        else:
            if Products.objects.filter(id=productid).exists():

                x = TemporaryC.objects.get(id=1)
                customer = Customer.objects.get(Q(customerName=x.customerName) & Q(customerPassword=x.customerPassword))

                y = Products.objects.get(id=productid)

                order = OrderProducts(productName=y.productName, productPrice=y.productPrice,
                                      sellerId=y.sellerId, customerId=customer.id)

                order.save()
                messages.info(request, "Product Ordered")
                return redirect("showproduct")

            else:
                messages.info(request, "Invalid Product Id")

            products = Products.objects.filter()
            context = {'products': products}

            return render(request, 'products/showproductlist.html', context)

def sellerProduct(request):
    if request.method == "GET":

        x = TemporaryS.objects.get(id=1)
        seller = Seller.objects.get(Q(sellerName=x.sellerName) & Q(sellerPassword=x.sellerPassword))

        products = Products.objects.filter(sellerId=seller.id)
        context = {'products': products}

        return render(request,'products/sellerproductlist.html',context)

    else:
        productid = request.POST["productid"]

        products = Products.objects.get(id=productid)
        products.delete()
        messages.info(request, "Product Removed")


    x = TemporaryS.objects.get(id=1)
    seller = Seller.objects.get(Q(sellerName=x.sellerName) & Q(sellerPassword=x.sellerPassword))

    products = Products.objects.filter(sellerId=seller.id)
    context = {'products': products}

    return render(request, 'products/sellerproductlist.html', context)


def showOrder(request):

    x = TemporaryS.objects.get(id=1)
    seller = Seller.objects.get(Q(sellerName=x.sellerName) & Q(sellerPassword=x.sellerPassword))

    if request.method == "GET":

        seller_order = OrderProducts.objects.filter(sellerId=seller.id)

        context = {'seller_order': seller_order,'seller':seller}

        return render(request,'products/showorder.html',context)

    else:
        orderid = request.POST["orderid"]

        if OrderProducts.objects.filter(id=orderid).exists():

            y = OrderProducts.objects.get(id=orderid)

            sell = BuyProducts(productName=y.productName, productPrice=y.productPrice,
                               sellerId=y.sellerId, customerId=y.customerId)

            sell.save()
            y.delete()
            messages.info(request, "Product Sold")
            return redirect("showorder")

        else:
            messages.info(request, "Invalid Order Id")

        seller_order = OrderProducts.objects.filter(sellerId=seller.id)
        context = {'seller_order': seller_order, 'seller': seller}

        return render(request, 'products/showorder.html', context)


def buyProduct(request):
    if request.method == "GET":

        x = TemporaryC.objects.get(id=1)
        productPrice = 0

        customer = Customer.objects.get(Q(customerName=x.customerName) & Q(customerPassword=x.customerPassword))

        customer_buy = BuyProducts.objects.filter(customerId=customer.id)

        for cb in customer_buy:
            productPrice += cb.productPrice

        totalProduct = len(customer_buy)

        context = {'customer_buy': customer_buy,'customer' : customer,'productPrice':productPrice,'totalProduct':totalProduct}

        return render(request,"products/buyproduct.html",context)


    return render(request,"products/buyproduct.html")

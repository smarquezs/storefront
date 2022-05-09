from django.shortcuts import render
from store.models import Customer, Product

def hello_world(request):
    products = Product.objects.order_by('-title')[:5]

    return render(request, 'hello.html', {'products': list(products)})
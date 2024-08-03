from django.shortcuts import render
from store.models import Product
# .filter(is_available=True)

def home(request):
    products = Product.objects.all()

    context = {
        "products": products,

    }
    return render(request, "home.html", context)

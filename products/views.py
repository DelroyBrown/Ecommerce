from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.db.models import Q
from .models import Product

def all_products(request):

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter a search query!")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)


    context = {
        'products' : products,
        'search_form' : query,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product' : product
    }

    return render(request, 'products/product_detail.html', context)

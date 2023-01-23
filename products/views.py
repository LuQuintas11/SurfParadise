from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponseRedirect, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Product, Review, Category
from .forms import ReviewForm
from django import forms
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ProductForm

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        
    }

    return render(request, 'products/products.html', context)




def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, id=product_id)
    favorite = bool(product.favourites.filter(id=request.user.id))

    if request.method == 'POST':

        body = request.POST.get('body', '')
        print(request.POST)
        if body:
            reviews = Review.objects.filter(
                
                product=product)
            review = Review.objects.create(
                    product=product,
                    body=body,
                )

            return redirect('product_detail', product_id=product_id)


    context = {
        'product': product,
        'favorite': favorite,
    }

    return render(request, 'products/product_detail.html', context)



@login_required
def favourite_add(request, id):
    product = get_object_or_404(Product, id=id)
    if product.favourites.filter(id=request.user.id).exists():
        product.favourites.remove(request.user)
    else:
        product.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])



def add_product(request):
    """ Add a product to the store """
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
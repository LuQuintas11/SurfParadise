from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponseRedirect, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Product, Review, Category
from .forms import ReviewForm
from django import forms
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


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
        rating = request.POST.get('rating', 3)
        body = request.POST.get('body', '')
        print(request.POST)
        if body:
            reviews = Review.objects.filter(
                # created_by=request.user, 
                product=product)
            
            if reviews.count() > 0:
                review = reviews.first()
                review.rating = rating
                review.body = body
                review.save()
            else:
                review = Review.objects.create(
                    product=product,
                    rating=rating,
                    body=body,
                    # created_by=request.user
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



@login_required
def favourite_list(request):
    favourite = Product.newmanager.filter(favourites=request.user)

    # list to hold the favourites
    favourites = []

    # get the current user
    user = User.objects.get(id=request.user.id)
    # get all products
    all_products = list(Product.objects.all())

    # loop over the products
    for product in all_products:
        # loop over the m2m list of the product
        for fav in product.favourites.all():
            # if the user is in the m2m list
            if fav.id == user.id:
                # add the product to the favourites list
                favourites.append(product)

    
    print(favourites)


    return render(request,
                  'products/favourites.html',
                  {'favourite': favourite})
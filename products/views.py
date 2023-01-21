from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from .models import Product
from .forms import ReviewForm
from django import forms
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required


# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    category = request.GET.get("category", None)
    if category:
        products = products.filter(category__name=category) 

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)




def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def post(self, request, slug, *args, **kwargs):
    ueryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    reviews = post.reviews.filter(approved=True).order_by("-created_on")
        

    reviews_form = ReviewForm(data=request.POST)
    if review_form.is_valid():
        review_form.instance.email = request.user.email
        review_form.instance.name = request.user.username
        review = review_form.save(commit=False)
        review.post = post
        review.save()
    else:
        review_form = CommentForm()

    return render(
        request,
        'products/product_detail.html',
        {   
               
            "post": post,
            "comments": reviews,
            "commented": True,
            "comment_form": review_form,
            

            },
        )



@ login_required
def favourite_add(request, id):
    post = get_object_or_404(Product, id=id)
    if post.favourites.filter(id=request.user.id).exists():
        post.favourites.remove(request.user)
    else:
        post.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@ login_required
def favourite_list(request):
    new = Product.newmanager.filter(favourites=request.user)
    return render(request,
                  'products/favourites.html',
                  {'new': new})
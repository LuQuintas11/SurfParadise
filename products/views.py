from django.shortcuts import (
    render,
    reverse,
    get_object_or_404,
    HttpResponseRedirect,
    redirect,
)
from django.contrib import messages
from django.db.models import Q
from .models import Product, Review, Category
from .forms import ReviewForm
from django import forms
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ProductForm


def all_products(request):
    """A view to show all products, including sorting and search queries"""

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))
            if sortkey == "category":
                sortkey = "category__name"
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

    if request.GET:
        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "You didn't enter any search criteria!")  # noqa
                return redirect(reverse("products"))

            queries = Q(name__icontains=query) | Q(description__icontains=query)  # noqa
            products = products.filter(queries)

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
    }

    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """A view to show individual product details"""

    product = get_object_or_404(Product, id=product_id)
    favorite = request.user in product.favourites.all()

    reviews = Review.objects.filter(product=product)

    context = {"product": product, "favorite": favorite, "reviews": reviews}
    return render(request, "products/product_detail.html", context)


@login_required
def favourite_add(request, id):
    product = get_object_or_404(Product, id=id)
    if request.user in product.favourites.all():
        product.favourites.remove(request.user)
    else:
        product.favourites.add(request.user)
    product.save()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


@login_required
def add_product(request):
    """Add a product to the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Successfully added product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request,
                "Failed to add product. Please ensure the form is valid."
            )
    else:
        form = ProductForm()

    template = "products/add_product.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """Edit a product in the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request,
                "Failed to update product. Please ensure the form is valid."
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f"You are editing {product.name}")

    template = "products/edit_product.html"
    context = {
        "form": form,
        "product": product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """Delete a product from the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, "Product deleted!")
    return redirect(reverse("products"))


@login_required
def createreview(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "GET":
        return render(
            request,
            "products/createreview.html",
            {"form": ReviewForm(), "product": product},
        )
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.product = product
            newReview.save()
            return redirect("product_detail", newReview.product.id)
        except ValueError:
            return render(
                request,
                "products/createreview.html",
            )


@login_required
def updatereview(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    if request.method == "GET":
        form = ReviewForm(instance=review)
        return render(
            request, "products/updatereview.html", {"review": review, "form": form}  # noqa
        )
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            messages.success(request, "Successfully updated review!")
            return redirect("product_detail", review.product.id)
        except ValueError:
            return render(
                request,
                "products/updatereview.html",
                {"review": review, "form": form, "error": "Bad data in form"},
            )


@login_required
def deletereview(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    messages.success(request, "Successfully delete review!")
    return redirect("product_detail", review.product.id)

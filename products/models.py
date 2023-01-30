from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):

   
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(id=0)

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )



    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    favourites = models.ManyToManyField(
        User, related_name='favourite', default=None, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    objects = models.Manager()  # default manager
    newmanager = NewManager()  # custom manager


    def __str__(self):
        return self.name


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

class Review(models.Model):
    
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE,null=True, blank=True )
    email = models.EmailField(default="user")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
      User,on_delete=models.CASCADE,null=True, blank=True )
   

   

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Review {self.body} "




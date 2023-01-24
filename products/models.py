from django.db import models
from django.contrib.auth.models import User

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




class Review(models.Model):
    
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    email = models.EmailField(default="user")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
   

   

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Review {self.content} "




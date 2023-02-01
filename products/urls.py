from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.all_products, name="products"),
    path("<int:product_id>", views.product_detail, name="product_detail"),
    path("fav/<int:id>/", views.favourite_add, name="favourite_add"),
    path("add/", views.add_product, name="add_product"),
    path("edit/<int:product_id>/", views.edit_product, name="edit_product"),
    path("delete/<int:product_id>/", views.delete_product, name="delete_product"),
    path("<int:product_id>/create", views.createreview, name="createreview"),
    path("review/<int:review_id>", views.updatereview, name="updatereview"),
    path("review/<int:review_id>/delete", views.deletereview, name="deletereview"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

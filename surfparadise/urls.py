from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import handler404

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("home.urls")),
    path("products/", include("products.urls")),
    path("bag/", include("bag.urls")),
    path("contact/", include("contact.urls")),
    path("checkout/", include("checkout.urls")),
    path("profile/", include("profiles.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'surfparadise.views.handler404'

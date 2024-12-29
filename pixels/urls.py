from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import redirect


def home_redirect(self):
    return redirect("/pix")


urlpatterns = [
    path("", home_redirect),
    path("pix/", include("pix.urls")),
    path("admin/", admin.site.urls),
    path("pix/wform/", include("wform.urls")),
    #    path('', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

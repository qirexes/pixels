from django.urls import path
from . import views
from .views import deposit
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'pix'
urlpatterns = [
    path("", views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path("collections/", views.collections , name='collections'),
    path('full_collection/<str:image_name>/', views.full_collection, name='full_collection'),
    path("create/", views.create , name='create'),
    path("dashboard/", views.dashboard , name='dashboard'),
    path("explore/", views.explore , name='explore'),
    path("notifications/", views.notifications , name='notifications'),
    path("Privacy/", views.privacy , name='Privacy'),
    path('settings/', views.settings_view, name='settings'),
    path('logout/', views.custom_logout, name='logout'),
    path('notifications/', views.notifications_view, name='notifications'),
    path("Terms/", views.Terms , name='Terms'),
    path('view_collections/<str:image_name>/', views.view_collections, name='view_collections'),
    path("collection_purchase/", views.collection_purchase , name="collection_purchase"),
    path('deposit/', deposit, name='deposit'),
    path('withdraw/', views.withdraw, name='withdraw'),
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

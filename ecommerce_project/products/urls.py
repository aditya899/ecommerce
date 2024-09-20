# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import ProductViewSet
from django.urls import path
from . import views
from django.conf import settings

# router = DefaultRouter()
# router.register(r'products', ProductViewSet)

urlpatterns = [
 path('', views.get_list),
 path('post/', views.post_product),
 path('edit/', views.update_product),
 path('delete/', views.delete_product),
]
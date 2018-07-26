
from django.conf.urls import url, include
from API import views
from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'customers', views.customers)
router.register(r'orders', views.orders)
router.register(r'product_type', views.Product_TypeViewSet)


urlpatterns = [
    url(r'^', include(router.urls))
]
# Authors Raf and Cashew <3



# Takes us to the customers method on the view page when the url ends in "customers"

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

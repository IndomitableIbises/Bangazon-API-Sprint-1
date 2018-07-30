
from django.conf.urls import url, include
from API import views
from rest_framework import routers
from rest_framework.routers import DefaultRouter


# Authors Raf and Cashew <3
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)

# Takes us to the customers method on the view page when the url ends in "customers"
router.register(r'customers', views.customers)
router.register(r'product_types', views.Product_TypeViewSet)
router.register(r'computers', views.ComputerViewSet)
router.register(r'departments', views.DepartmentViewSet)
router.register(r'orders', views.orders)
router.register(r'product_type', views.Product_TypeViewSet)

# Author Cashew <3
# Takes us to the pay_type method on the view page when the url ends in "payment_types"
router.register(r'payment_type', views.pay_types)


###########################################################################
# EMPLOYEE SIDE URLS
###########################################################################

# Author Raf - Employee Url
router.register(r'employee', views.Employee)


urlpatterns = [
    url(r'^', include(router.urls))
]




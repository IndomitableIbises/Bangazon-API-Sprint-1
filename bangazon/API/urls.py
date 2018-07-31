
from django.conf.urls import url, include
from API import views
from rest_framework import routers
from rest_framework.routers import DefaultRouter


router = routers.DefaultRouter()

###########################################################################
# CUSTOMER SIDE URLS
###########################################################################

# Takes us to the customers method on the view page when the url ends in "customers"
router.register(r'customers', views.customers)

#  Author: Raf - InactiveURL
# Takes us to the Inactive Customers
router.register(r'inactive_customers', views.inactive_customers, base_name='inactive')

router.register(r'product_type', views.Product_TypeViewSet)

# Authors Raf and Cashew <3
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
router.register(r'products', views.ProductViewSet)

# Author Cashew <3
# Takes us to the pay_type method on the view page when the url ends in "payment_types"
router.register(r'payment_type', views.pay_types)

router.register(r'orders', views.orders)


###########################################################################
# EMPLOYEE SIDE URLS
###########################################################################

# Author Raf - Employee Url
router.register(r'employee', views.Employee)

router.register(r'departments', views.DepartmentViewSet)
router.register(r'computers', views.ComputerViewSet)

# Author Raf & Cashew <3 - Training_Prog Url
router.register(r'training', views.Training_Prog)

# Author Raf & Cashew <3 - Emp_Training Url
router.register(r'employee_training', views.Emp_Train)


urlpatterns = [
    url(r'^', include(router.urls))
]




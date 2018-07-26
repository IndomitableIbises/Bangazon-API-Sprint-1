# Authors Raf and Cashew <3

from django.conf.urls import url, include
from API import views
from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = routers.DefaultRouter()

# Takes us to the customers method on the view page when the url ends in "customers"
router.register(r'customers', views.customers)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]
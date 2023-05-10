from . import views
from django.urls import path


urlpatterns = [
    path('', views.listing_list, name='listings'),
]

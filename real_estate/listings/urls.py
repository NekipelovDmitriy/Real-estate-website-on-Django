from . import views
from django.urls import path


urlpatterns = [
    path('', views.listing_list, name='listings'),
    path('listings/<pk>/', views.listing_retrieve , name='listing'),
    path('listing/<pk>/edit', views.listing_update, name='update'),
    path('listing/<pk>/delete', views.listing_delete, name='delete'),
    path('create', views.listing_create, name='listing_create'),    
]

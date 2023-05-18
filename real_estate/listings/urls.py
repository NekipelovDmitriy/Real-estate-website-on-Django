from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('listings/', views.listing_list, name='listings'),
    path('listings/<pk>/', views.listing_retrieve , name='listing'),
    path('listing/<pk>/edit/', views.listing_update, name='update'),
    path('listing/<pk>/delete/', views.listing_delete, name='delete'),
    path('create/', views.listing_create, name='listing_create'),    
    path('agents/create/', views.agent_create, name='agent_create'),
    path('agents/', views.agents_list, name='agents_list'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

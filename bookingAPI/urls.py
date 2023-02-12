from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'bookings', views.BookingsViewSet, basename='booking')
router.register(r'menus', views.MenusViewSet, basename='menu')

urlpatterns = [
]

urlpatterns += router.urls
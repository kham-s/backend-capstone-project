from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()

router.register(r'bookings', views.BookingsViewSet, basename='booking')
router.register(r'menus', views.MenusViewSet, basename='menu')

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
    path('bookings/', views.bookings, name="bookings"),
    path('reservations/', views.reservations, name="reservations"),
    path('api-token-auth/', obtain_auth_token),
    path('api/', include(router.urls))
]
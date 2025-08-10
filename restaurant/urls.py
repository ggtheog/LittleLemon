from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'menu', MenuViewSet)
router.register(r'booking', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

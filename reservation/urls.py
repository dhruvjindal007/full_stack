#define URL route for index() view
from django.urls import path,include
from . import views
from rest_framework import routers
from .views import UserViewSet,BookingViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tables', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include(router.urls)),
    path('booking/', include(router.urls)),
]

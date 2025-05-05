from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionViewSet, RegisterView, get_summary

router = DefaultRouter()
router.register(r'user/transactions', TransactionViewSet, basename='transactions')

urlpatterns = [
    path('user/register/', RegisterView.as_view(), name='register'),
    path('user/summary/', get_summary, name='summary'),
    path('', include(router.urls)),
]

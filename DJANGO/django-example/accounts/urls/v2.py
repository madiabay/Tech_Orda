from django.urls import path, include
from rest_framework_nested import routers

from accounts import views


router = routers.DefaultRouter()
router.register('wallets', views.WalletViewSet, basename='wallets-v2')
router.register('accounts', views.AccountViewSetV2, basename='accounts-v2')

urlpatterns = [
    path('', include(router.urls)),
]
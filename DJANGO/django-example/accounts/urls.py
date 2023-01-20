from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from accounts import views


router = routers.DefaultRouter()
router.register('wallets', views.WalletViewSet_2, basename='wallets')
router.register('wallets', views.WalletViewSet, basename='account-wallets')
router.register('accounts', views.AccountViewSet)

account_router = routers.NestedDefaultRouter(router, 'accounts', lookup='account')
account_router.register('wallets', views.WalletViewSet, basename='account-wallets')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(account_router.urls)),
]
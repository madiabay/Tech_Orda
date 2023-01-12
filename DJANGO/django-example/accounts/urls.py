from rest_framework.routers import DefaultRouter
from accounts import views


router = DefaultRouter()
router.register('wallets', views.WalletViewSet)
router.register('accounts', views.AccountViewSet)

urlpatterns = router.urls
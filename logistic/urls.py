from rest_framework.routers import DefaultRouter
from django.urls import include, path

from logistic.views import ProductViewSet, StockViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)

urlpatterns = router.urls

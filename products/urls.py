from . import signals

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, ReviewViewSet, CategoryViewSet, OrderViewSet
from .services.product_view_history import ProductViewHistoryCreate
from .services.flash_sale import check_flash_sale, FlashSaleListCreateView
from .services import admin_replenish_stock

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('sale/', FlashSaleListCreateView.as_view(), name='sale'),
    path('check-sale/<int:product_id>/', check_flash_sale, name='product-view-history-create'),
    path('product-view/', ProductViewHistoryCreate.as_view(), name='product-view-history-create'),
    path('admin/replenish_stock/<int:product_id>/<int:amount>', admin_replenish_stock, name='admin_replenish_stock'),

]
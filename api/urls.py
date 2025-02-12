from tkinter.font import names

from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path('products/', views.ProductListCreateAPIView.as_view(), name='products'),path('products/info/', views.ProductInfoAPIView.as_view(), name='info'),
    path('products/<int:product_id>', views.ProductDetailAPIView.as_view(), name='product'),
    path('orders/', views.OrderListAPIView.as_view(), name='orders'),
    path('user-orders/', views.UserOrderListAPIView.as_view(), name='user-orders'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

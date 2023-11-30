from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns= [
         path('', views.dashboard, name='dashboard' ),
         path('login/', views.CustomLoginView.as_view(), name='login'),
         path('logout/', LogoutView.as_view(next_page='dashboard'), name='logout'),

         path('inventory/', views.StockListView.as_view(), name='inventory'),
         path('new-stock', views.StockCreateView.as_view(), name='new-stock'),
         path('inventory/<int:pk>/edit', views.StockUpdateView.as_view(), name='update-stock'),
         path('inventory/<int:pk>/delete', views.DeleteStockView.as_view(), name='delete-stock'),

         path('purchases/', views.PurchaseView.as_view(), name='purchases-list'),
         path('purchases/new/pk', views.PurchaseCreateView.as_view(), name='new-purchase'),
         path("purchases/<billno>", views.PurchaseBillView.as_view(), name="purchase-bill"),
]
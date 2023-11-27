from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns= [
         path('', views.dashboard, name='dashboard' ),
         path('login/', views.CustomLoginView.as_view(), name='login'),
         path('logout/', LogoutView.as_view(next_page='dashboard'), name='logout'),

         path('inventory/', views.StockListView.as_view(), name='inventory'),
]
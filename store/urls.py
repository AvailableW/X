from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('category/<slug:slug>/', views.category, name='category'),
    path('<slug:slug>/<int:id>/', views.product_detail, name='product_detail'),
]

from django.urls import path
from .views import foods

urlpatterns = [
    # path('', views.index, name='index'),
    path('foods/', foods.CafeteriasView.as_view(), name='index'),
    path('foods/<int:pk>/', foods.CafeteriaView.as_view(), name='food')
]

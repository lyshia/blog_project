from django.urls import path
from .views import gifts

urlpatterns = [
    # path('', views.index, name='index'),
    path('gifts/', gifts.GiftsView.as_view(),  name = 'index'),
    path('gifts/<int:pk>/', gifts.GiftView.as_view(), name='gift')
]

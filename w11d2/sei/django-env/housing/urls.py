from django.urls import path
from django.urls import path
from .views import dorms

urlpatterns = [
    path('dorms/', dorms.DormsView.as_view(), name='index'),
    path('dorms/<int:pk>/', dorms.DormView.as_view(), name='dorm-view')
]

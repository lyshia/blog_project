from django.urls import path

from hospital.views import patients
from .views import doctors

urlpatterns = [
    # path('', views.index, name='index'),
    path('doctors/', doctors.HospitalsView.as_view(), name='index'),
    # path('<int:pk>', views.show, name='doctors')
    path('doctors/<int:pk>/', doctors.HospitalView.as_view(), name='doctor-detail'),
    path('patients/', patients.PatientsView.as_view(), name='patients'),
    # path('<int:pk>', views.show, name='doctors')
    path('patients/<int:pk>/', patients.PatientView.as_view(), name='patients-detail')
]

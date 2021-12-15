from django.urls import path
from .views.user import SignIn, SignOut, Signup, ChangePassword

urlpatterns = [
    path('sign-up/', Signup.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out', SignOut.as_view(), name ='sign-out'),
    path('change-password/', ChangePassword.as_view(), name='change-password')
]
from django.urls import path

from accounts.views import UserSignUp, sign_out_view, UserSignIn

urlpatterns = (
    path('sign_up/', UserSignUp.as_view(), name='user sign up'),
    path('sign_out/', sign_out_view, name='user sign out'),
    path('sign_in/', UserSignIn.as_view(), name='user sign in'),
)

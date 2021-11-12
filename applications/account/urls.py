from django.urls import path
from applications.account.views import RegistrationView, ActivationView, LoginView, LogoutView

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('activate/<str:activation_code>/', ActivationView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view())
]
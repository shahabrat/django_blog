from django.urls import path
from .views import SignUpView
from pages.views import PasswordChangeView
urlpatterns=[
    path('signup/',SignUpView.as_view(),name='signup'),
    #path('password_change/',PasswordChangeView.as_view())
]
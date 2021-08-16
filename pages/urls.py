from django.urls import path
from .views import HomePageView,PasswordChangeView

urlpatterns=[
    path('',HomePageView.as_view(),name='home'),
    #path('password_change/',PasswordChangeView.as_view())
]
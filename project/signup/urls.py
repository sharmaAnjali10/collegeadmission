from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
urlpatterns=[
    path('',home, name='home'),
    path('signup/', SignupView.as_view() ,name='sign'),
    path('login/', Mylogin.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='/login/'),name='logout'),
   path('registration/',CourseRegistration.as_view(),name='registration'),
]
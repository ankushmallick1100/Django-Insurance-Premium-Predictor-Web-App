from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('aboutus/', views.aboutus, name = 'aboutus'),
    path('contactus/', views.contactus, name = 'contactus'),
    path('insurance-prediction/', views.insurancePrediction, name='insurance_prediction'),
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_from_page, name='logout')
]
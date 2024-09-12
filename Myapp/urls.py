
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_pro, name='index_pro'),
    path('login_page/',views.login_page,name='login_page'),
    path('register/',views.register,name='register'),
    path('chat/', views.chatbot_view, name='chatbot_view'),  # Display the chatbot interface
    path('contact/', views.contact_us, name='contact_us'),
    path('appointment/', views.appointment_view, name='appointment_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('appointment/success/', views.appointment_success, name='appointment_success'),





    

]

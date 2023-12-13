from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('schedule_appointment',views.schedule_appointment,name='schedule_appointment'),
   path('appointment_success',views.appointment_success,name='appointment_success'),
   path('create_patient',views.create_patient,name='create_patient'),
   path('create_doctor',views.create_doctor,name='create_doctor')
]

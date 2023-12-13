from django.shortcuts import render, redirect
from .models import Doctor, Patient, Appointment
def create_doctor(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        specialization = request.POST.get('specialization')
        experience = request.POST.get('experience')
        
        doctor = Doctor(name=name, specialization=specialization, experience=experience)
        doctor.save()
        
        return redirect('create_doctor')  # Replace 'doctor_list' with the URL name of the doctor list view
        
    return render(request, 'scheduler2app/create_doctor.html')
def create_patient(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        
        patient = Patient(name=name, age=age, gender=gender)
        patient.save()
        
        return redirect('create_patient')  # Replace 'patient_list' with the URL name of the patient list view
        
    return render(request, 'scheduler2app/create_patient.html')
def schedule_appointment(request):
    if request.method == 'POST':
        doctor_name = request.POST['doctor']
        patient_name = request.POST['patient']
        date = request.POST['date']
        time = request.POST['time']

        doctor = Doctor.objects.get_or_create(name=doctor_name)[0]
        patient = Patient.objects.get_or_create(name=patient_name)[0]

        appointment = Appointment.objects.create(doctor=doctor, patient=patient, date=date, time=time)
        return redirect('appointment_success')
    
    return render(request, 'scheduler2app/schedule_appointment.html')

def appointment_success(request):
    return render(request, 'scheduler2app/appointment_success.html')


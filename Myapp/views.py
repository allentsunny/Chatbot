from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
# from django.contrib.auth.hashers import make_password
from . forms import SignupForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def index_pro(request):
    return render(request,'index_pro.html')
 
# Create your views here.
def login_page(request):
    if request.method == 'POST':       
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']   
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('chatbot_view')
            else:
                # Display an error message if authentication fails
                messages.error(request, 'Invalid username or password. Please try again.')
        else:
            # Display an error message if the form is invalid
            messages.error(request, 'Invalid form submission. Please check your input.')        
    else:
        form = LoginForm()
    return render(request, 'login_page.html', {'form': form})

def register(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=User(username=username,email=email)
            user.set_password(password)
            user.save()
            return redirect('login_page')
    else:
        form=SignupForm()
    return render(request,'register.html',{'form':form})
from django.http import JsonResponse
from django.shortcuts import render
from .nltk_bot import chatbot_response
from .models import Appointment
from django.shortcuts import render
from django.http import JsonResponse
from .models import Appointment
from .nltk_bot import chatbot_response

@login_required

def chatbot_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('message')
        specialization = request.POST.get('specialization')
        date = request.POST.get('date')
        name = request.POST.get('name')
        contact_number = request.POST.get('contact_number')
        email = request.POST.get('email')

        print(f"User Input: {user_input}")
        print(f"Specialization: {specialization}")
        print(f"Date: {date}")
        print(f"Name: {name}")
        print(f"Contact Number: {contact_number}")
        print(f"Email: {email}")

        user_data = {
            'specialization': specialization,
            'date': date,
            'name': name,
            'contact_number': contact_number,
            'email': email
        }

        bot_response = chatbot_response(user_input, user_data)

        if "Your appointment for" in bot_response:
            if specialization and date and contact_number and email:
                Appointment.objects.create(
                    specialization=specialization,
                    date=date,
                    contact_number=contact_number,
                    email=email
                )

            return redirect('appointment_view')
        return JsonResponse({'response': bot_response})

    return render(request, 'chatbot.html')


from django.shortcuts import render, redirect
from .forms import AppointmentForm
from django.http import HttpResponse

from django.shortcuts import render
from django.http import HttpResponse
from .forms import AppointmentForm
from .models import Appointment

def appointment_view(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            # Clear session data after saving
            request.session.pop('appointment_data', None)
            return HttpResponse("Appointment successfully booked.")
    else:
        # Prepopulate form with data from session
        appointment_data = request.session.get('appointment_data', {})
        form = AppointmentForm(initial=appointment_data)

    return render(request, 'appointment.html', {'form': form})


# views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact_us')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})

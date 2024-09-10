from django import forms
class SignupForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['specialization', 'date', 'contact_number', 'email']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'specialization': forms.Select(choices=Appointment.SPECIALIZATION_CHOICES),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['specialization'].empty_label = "Select specialization"

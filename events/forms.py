from django import forms 
from events.models import Registration

class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'phone', 'email', 'college', 'image']


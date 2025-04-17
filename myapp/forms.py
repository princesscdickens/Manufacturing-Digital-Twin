from django import forms

class SensorReadingForm(forms.Form):
    temperature = forms.FloatField(label="Temperature (°F)")
    vibration = forms.FloatField(label="Vibration (g)")

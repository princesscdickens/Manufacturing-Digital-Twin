# Create your views here.
from django.shortcuts import render
from .forms import SensorReadingForm
from .utils import predict_failure

def sensor_view(request):
    result = None
    if request.method == "POST":
        form = SensorReadingForm(request.POST)
        if form.is_valid():
            temp = form.cleaned_data["temperature"]
            vib = form.cleaned_data["vibration"]
            prediction = predict_failure(temp, vib)
            result = "Healthy" if prediction == 0 else "Failure Predicted!"
    else:
        form = SensorReadingForm()
    
    return render(request, "myapp/dashboard.html", {"form": form, "result": result})

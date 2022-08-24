from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from doctors.models import Doctor

# Create your views here.
def index(request):
    
    doctors = Doctor.objects.all()
    
    context = {
        'doctors': doctors
    }
    return render(request, 'doctors/index.html', context)


def edit(request):
    return HttpResponse("Hello Doctors EDIT")

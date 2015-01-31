from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'services/index.html')


def exambank(request):
    return render(request, 'services/exambank.html')


def lockers(request):
    return render(request, 'services/lockers.html')


def bookings(request):
    return render(request, 'services/bookings.html')

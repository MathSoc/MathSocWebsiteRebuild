from django.shortcuts import render


def index(request):
    return render(request, 'frontend/index.html')


def resources(request):
    return render(request, 'frontend/resources.html')


def governance(request):
    return render(request, 'frontend/governance.html')


def office(request):
    return render(request, 'frontend/office.html')


def volunteers(request):
    return render(request, 'frontend/volunteers.html')


def clubs(request):
    return render(request, 'frontend/clubs.html')


def contact(request):
    return render(request, 'frontend/contact.html')

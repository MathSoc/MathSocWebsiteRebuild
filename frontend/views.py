from django.shortcuts import render
from django.contrib.auth.models import User
from tangent.models import Position, Member, Organization


def index(request):
    return render(request, 'frontend/index.html')


def governance(request):
    gov = Organization.objects.filter(classification__icontains="math")
    context_dict = {'orgs': gov}
    return render(request, 'frontend/governance.html', context_dict)


def organization(request, org_id):
    org = Organization.objects.get(id=org_id)
    context_dict = {
        'org' : org
    }
    return render(request,
                  'frontend/organization.html',
                  context_dict)


def office(request):
    return render(request, 'frontend/office.html')


def volunteers(request):
    return render(request, 'frontend/volunteers.html')


def clubs(request):
    c = Organization.objects.filter(classification__icontains="club")
    context_dict = {'clubs': c}
    return render(request, 'frontend/clubs.html', context_dict)


def contact(request):
    return render(request, 'frontend/contact.html')

from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from tangent.models import Position, Member, Organization
import logging

logger = logging.getLogger(__name__)

# ---------- HELPERS -----------------

def get_all_orgs_from_positions(positions):
    orgs = {}
    for pos in positions:
        org = pos.organization
        if org.name in orgs:
            orgs[org.name]['positions'].append(pos)
        else:
            orgs[org.name] = {
                'description': org.description,
                'positions': [pos]
            }
    return orgs

# --------- View Functions ------------

def index(request):
    return render(request, 'frontend/index.html')


def governance(request):
    gov = Organization.objects.filter(classification="MATH_GOV")
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
    org = None
    try:
        org = Organization.objects.get(name="MathSoc Office")
    except Organization.DoesNotExist:
        logger.error("org DNE")

    context_dict = {
        'org': org
    }
    return render(request, 'frontend/office.html', context_dict)


def volunteers(request):
    free_positions = Position.objects.filter(
        occupied_by=None,
        want_applications=True
    ).select_related('organization__name', 'organization__description')
    occupied_positions = Position.objects.exclude(
        occupied_by=None
    ).select_related('organization__name', 'organization__description')
    context_dict = {'free_position_orgs': get_all_orgs_from_positions(free_positions),
                    'occupied_position_orgs': get_all_orgs_from_positions(occupied_positions)}
    return render(request, 'frontend/volunteers.html', context_dict)

def position(request, pos_id):
    pos = Position.objects.get(id=pos_id)
    context_dict = {
        'pos': pos
    }
    return render(request, 'frontend/position.html', context_dict)


def clubs(request):
    c = Organization.objects.filter(classification__icontains="club")
    context_dict = {'clubs': c}
    return render(request, 'frontend/clubs.html', context_dict)


def contact(request):
    return render(request, 'frontend/contact.html')

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from tangent.models import Organization, Position
from services.models import BookingRequest
import datetime


@login_required
def home(request):
    user = User.objects.get(username=request.user.username)
    # TODO figure out what user permissions this is and that this works
    if False:  # user.user_permissions:
        # we need to show everything
        organizations = Organization.objects.all().order_by('name')
    else:
        # filter by what organizations the user is admin on
        organizations = Organization.objects.filter(positions__occupied_by__user=user).order_by('name')
    print organizations
    context_dict = {'organizations': organizations}
    return render(request, 'tangent/index.html', context_dict)


def organization(request, org_id):
    org = Organization.objects.get(id=org_id)
    context_dict = {
        'org' : org
    }
    return render(request,
                  'tangent/organization.html',
                  context_dict)

@login_required
def log(request):
    return render(request, 'tangent/log.html')

@login_required
def profile(request):
    return render(request, 'tangent/index.html')

@login_required
def help(request):
    return render(request, 'tangent/index.html')

@login_required
def website(request):
    return render(request, 'tangent/index.html')

@login_required
def bookings(request):
    # TODO: ADD parameter that gets rid of filter
    requests = BookingRequest.objects.filter(end__gte=datetime.datetime.today()).order_by('-start', 'status')
    return render(request, 'tangent/bookings.html', {'requests': requests})

@login_required
def booking(request, booking_id):
    booking = get_object_or_404(BookingRequest, id=booking_id)
    return render(request, 'tangent/booking.html', {'booking': booking})
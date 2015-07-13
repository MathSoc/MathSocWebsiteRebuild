from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from tangent.models import Organization, Position


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


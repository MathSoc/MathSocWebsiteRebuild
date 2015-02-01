from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from tangent.models import Organization

@login_required
def home(request):
    organizations = Organization.objects.filter(positions=request.user).order_by('name')
    print organizations
    context_dict = {'organizations': organizations}
    return render(request, 'tangent/index.html', context_dict)


def organization(request, org_id):

    return render(request,
                  'tangent/organization.html',
                  {})

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


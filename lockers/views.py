from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
from lockers.models import Locker
from tangent.models import Member


@login_required()
def lockers(request):
    # get_or_create returns a tuple (object, created) where created
    #   is a boolean
    member = Member.objects.get_or_create(user=request.user)[0]

    if request.method == 'POST':
        # Return JSON object which will be parsed
        if not member.has_locker:
            # give them a locker
            locker = Locker.objects.filter(owner=None)[0]
            locker.owner = member
            member.has_locker = True
            member.used_resources = True
            locker.save()
            member.save()
            ret = {'result': "Your locker has been reserved. You will receive an email "
                             "soon with details."}
        else:
            ret = {'result': "You already have a locker"}

        return HttpResponse(json.dumps(ret), content_type='application/json')

    else:  # not a post request
        lockers = True if Locker.objects.filter(owner=None) else False
        contect_dict = {'lockers': lockers}
        return render(request, 'lockers/lockers.html', contect_dict)
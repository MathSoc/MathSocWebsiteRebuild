from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required()
def evaluations(request):
    return render(request, 'evaluations/evaluations.html')
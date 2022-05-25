from django.http import HttpResponse
from django.shortcuts import render

from home.models import UserProfile


def index(request):
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'profile': profile}
    return render(request, 'user_profile.html', context)

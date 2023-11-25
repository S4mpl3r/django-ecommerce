from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url="login")
def user_profile(request):
    return render(request, "user_profile/profile.html")

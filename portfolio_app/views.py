from django.shortcuts import render, redirect
from portfolio_app.models import *
from portfolio_app.forms import *

def home(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()

    context = {
        'profile': profile,
        'projects': projects,
    }
    return render(request, 'home.html', context)


def update_profile(request):
    profile = Profile.objects.first()  # Get existing profile or create a new one
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'update_profile.html', {'form': form})

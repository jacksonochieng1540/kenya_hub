
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from .models import User
from django.contrib.auth import get_user_model
from .models import Badge

def profile_view(request, username):
    profile_user = get_object_or_404(User, username=username)
    return render(request, 'accounts/profile.html', {'profile_user': profile_user})



# ===== User Registration =====
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

# ===== User Profile =====
def profile_view(request, username):
    profile_user = get_object_or_404(User, username=username)
    return render(request, 'accounts/profile.html', {'profile_user': profile_user})

# ===== Edit Profile =====
@login_required
def edit_profile(request):
    if request.method == 'POST':
        bio = request.POST.get('bio', '')
        location = request.POST.get('location', '')
        github = request.POST.get('github_link', '')
        linkedin = request.POST.get('linkedin_link', '')

        request.user.bio = bio
        request.user.location = location
        request.user.github_link = github
        request.user.linkedin_link = linkedin
        request.user.save()

        return redirect('profile', username=request.user.username)

    return render(request, 'accounts/edit_profile.html', {'user': request.user})

def leaderboard_view(request):
    User = get_user_model()
    top_users = User.objects.order_by('-reputation')[:20]  
    return render(request, 'accounts/leaderboard.html', {'top_users': top_users})


def badge_history_view(request, username):
    profile_user = get_object_or_404(User, username=username)
    badges = profile_user.badges.order_by('-awarded_at')
    return render(request, 'accounts/badge_history.html', {'profile_user': profile_user, 'badges': badges})

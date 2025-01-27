from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import SignupForm
from .models import Userprofile

from team.models import Team

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()

            team = Team.objects.create(name=f'Team {user.username}', created_by=user)
            team.members.add(user)
            team.save()
            
            Userprofile.objects.create(user=user, active_team=team)

            request.session['user_id'] = user.id
            
            return redirect('team:select_team_plan')
    else:
        form = SignupForm()

    return render(request, 'userprofile/signup.html', {
        'form': form
    })

@login_required
def myaccount(request):
    return render(request, 'userprofile/myaccount.html')
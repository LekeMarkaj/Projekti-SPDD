from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

from .forms import TeamForm
from .models import Team, Plan

@login_required
def teams_list(request):
    teams = Team.objects.filter(members__in=[request.user])

    return render(request, 'team/teams_list.html', {'teams': teams})

@login_required
def teams_activate(request, pk):
    team = Team.objects.filter(members__in=[request.user]).get(pk=pk)
    userprofile = request.user.userprofile
    userprofile.active_team = team
    userprofile.save()

    return redirect('team:detail', pk=pk)

@login_required
def detail(request, pk):
    team = get_object_or_404(Team, members__in=[request.user], pk=pk)
    plan = team.plan 

    return render(request, 'team/detail.html', {
        'team': team,
        'plan': plan,
    })

@login_required
def edit_team(request, pk):
    team = get_object_or_404(Team, created_by=request.user, pk=pk)

    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)

        if form.is_valid():
            form.save()

            messages.success(request, 'The changes was saved!')

            return redirect('userprofile:myaccount')
    else:
        form = TeamForm(instance=team)

    return render(request, 'team/edit_team.html', {
        'team': team,
        'form': form
    })


def select_team_plan(request):
    # Retrieve the user from the session
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('signup')  # Redirect to signup if no user ID in session

    user = get_object_or_404(User, id=user_id)
    userprofile = user.userprofile
    team = userprofile.get_active_team()

    if not team:
        return render(request, 'error.html', {'message': 'You need an active team to select a plan.'})

    if request.method == 'POST':
        # Retrieve the selected plan from the hidden input
        plan_id = request.POST.get('plan')
        try:
            selected_plan = Plan.objects.get(id=plan_id)  # Validate the plan exists
            team.plan = selected_plan  # Assign the selected plan to the team
            team.save()

            # Clear the session and redirect to login
            del request.session['user_id']
            return redirect('login')  # Redirect to the login page
        except Plan.DoesNotExist:
            return render(request, 'error.html', {'message': 'Invalid plan selected.'})


    context = {
        'plans': Plan.objects.all(),
        'team': team,
    }
    return render(request, 'team/select_team_plan.html', context)

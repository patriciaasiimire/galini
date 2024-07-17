from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserForm, TherapistForm
from .models import Therapist

@login_required
def profile(request):
    user = request.user
    therapist = Therapist.objects.get(user=user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        therapist_form = TherapistForm(request.POST, instance=therapist)
        if user_form.is_valid() and therapist_form.is_valid():
            user_form.save()
            therapist_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=user)
        therapist_form = TherapistForm(instance=therapist)

    context = {
        'user_form': user_form,
        'therapist_form': therapist_form
    }
    return render(request, 'theme/profile.html', context)

# view for displaying therapist profiles
def therapist_detail(request, pk):
    therapist = get_object_or_404(Therapist, pk=pk) 
    return render(request, 'therapists/detail.html', {'therapist': therapist})

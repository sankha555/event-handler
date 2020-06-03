from django.shortcuts import render, get_object_or_404, redirect
from users.models import Creator
from users.forms import CreatorRegistrationForm,CreatorProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from allauth.socialaccount.models import SocialAccount


def register(request):
    if request.method == 'POST':
        form = CreatorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, f'Complete Your Profile!')
            
            # logging the user in
            user = authenticate(username=username, password=form.cleaned_data['password1'])
            login(request, user)

            new_creator = Creator.objects.create(
                user = request.user,
                first_name = "",
                last_name = "",
                gmail_email = ""
            )
            new_creator.save()
            
            return redirect('profile')
    else :
        form = CreatorRegistrationForm()
    return render(request, 'users/register.htm', {'form' : form})

@login_required
def profile(request):
    profile = get_object_or_404(Creator, user = request.user)
    if request.method == 'POST':
        form = CreatorProfileForm(request.POST, instance = request.user.creator)

        if form.is_valid():
            form.save()

    else:
        form = CreatorProfileForm(instance=request.user.creator)

    context = {
        'form' : form
    }
    return render(request, 'users/profile.htm', context)

@login_required
def post_login(request):
    user = request.user
    reg_users = User.objects.all()
    emails = []
    for u in reg_users:
        if u.email is not None:
            emails.append(u.email)

    if user.email in emails:
        return redirect('dashboard')
    else:
        if sociallogin.account.provider == 'google':
            try:
                new_user = User.objects.get(email = sociallogin.email)
                return redirect('dashboard')
            except:
                user_data = user.socialaccount_set.filter(provider='google')[0].extra_data

                email = user_data['email']
                first_name = user_data['first_name']
                last_name = user_data['last_name']

                # Creating a new user profile and 
                new_user = User.objects.create_user(
                    username = email.split('@')[0],
                    email = email
                )
                new_user.save()

                profile = get_object_or_404(Creator, user = new_user)
                profile.first_name = first_name
                profile.last_name = last_name
                profile.gmail_email = email
                profile.save()

                return redirect('profile')

# Create your views here.

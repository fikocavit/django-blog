from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import authenticate, login , logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from App_login.forms import SignUpForm,ProfileChangeForm,PictureChangeForm

# Create your views here.


def sign_up(request):
    form=SignUpForm()
    registered=False
    if request.method=="POST":
        form=SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered=True
    return render(request, 'App_login/signup.html',context={
        'form': form,
        'registered' : registered
    })
    
def login_user(request):
    form=AuthenticationForm()
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user= authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
    
    return render(request, 'App_login/login.html',context={
        'form': form
    })
    
@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_login:login'))
         

@login_required
def user_profile(request):
    return render(request, 'App_login/profile.html',context={})


@login_required
def user_change(request):
    current_user=request.user
    form=ProfileChangeForm(instance=current_user)
    if request.method=="POST":
        form=ProfileChangeForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form=ProfileChangeForm(instance=current_user)
            return HttpResponseRedirect(reverse('App_login:profile'))
            
    return render(request, 'App_login/change_profile.html',context={
        'form': form
    })

@login_required
def change_password(request):
    current_user=request.user
    form=PasswordChangeForm(current_user)
    changed=False
    if request.method=="POST":
        form=PasswordChangeForm(current_user,data=request.POST)
        if form.is_valid():
            form.save()
            changed=True
            form=PasswordChangeForm(current_user)
    
    return render(request, 'App_login/password.html',context={
        'form': form,
        'changed': changed
    })
    
@login_required
def change_pic(request):
    form=PictureChangeForm()
    if request.method=="POST":
        form=PictureChangeForm(request.user)
    return render(request, 'App_login/change-pic.html',context={
        'form' : form
    })
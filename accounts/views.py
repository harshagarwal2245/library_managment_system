from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, ProfileForm, UserEditForm
from .models import Profile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from shelf.models import Book

def register(request):
    """ Register a new user we had used here model form and same form is rendered
    in html file. 
    
    """
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request,
                          'blog/account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = RegisterForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})

def user_login(request):
    """  A sample function to authenticate a user and if the user is valid then redirect to index page.
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


@login_required
def dashboard(request):
    object_list = Book.objects.filter(owner=request.user)
    paginator = Paginator(object_list,3)
    page=request.GET.get('page')
    try:
        books=paginator.page(page)
    except PageNotAnInteger:
        books=paginator.page(1)
    except EmptyPage:
        books=paginator.page(paginator.num_pages)
   
    return render(request,'account/dashboard.html',{'section':'dashboard','page':page,'books':books}) 
    

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST, instance=request.user,data=request.POST)
        profile_form = ProfileForm(request.POST, instance=request.user.profile,data=request.POST,files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return render(request,
                          'account/register_done.html',
                          {'new_user': request.user})
    else:
        user_form = RegisterForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request,
                  'account/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})


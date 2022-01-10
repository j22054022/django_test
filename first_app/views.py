from os import access
from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import *
from first_app.form import *
import pprint
# for Login require
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.

def index(req): 
    # this is index view for django project

    return render(req, 'index.html', context={})

def first_app_index(request): 
    output = 'This is index of first_app'
    topic_list = Topic.objects.order_by('top_name')
    webpage_list = AccessRecorder.objects.order_by('date')
    first_app_dict = {
        'variable': 'This is a string from view',
        'topic_list': topic_list, 
        'date_dict' : {
            'access_records': webpage_list
        },
        'user_form_page': user_form_page
    }
    return render(request, 'first_app/index.html', context=first_app_dict)

def getWSGIRequest(request): 
    # output = str(vars(request)).replace('{', '{ \n\t').replace(', ', ', \n\t')
    output = str(vars(request))
    output = '<pre>{}</pre>'.format(output)
    # pp = pprint.PrettyPrinter()
    # pp.pprint(vars(request))
    return HttpResponse(output)
    # return HttpResponseRedirect(reverse('index'))

def user(request): 
    user_list = User.objects.order_by('first_name')
    user_dict = {
        'user_list': user_list
    }
    return render(request, 'first_app/user.html', context=user_dict)

def form_page(req): 
    # pp = pprint.PrettyPrinter()
    form = UserForm()
    form_dict = {
        'form': form,
        'data': {}, 
    }
    
    if req.method == 'POST': 
        # pp.pprint(vars(req))
        # pp.pprint(dir(req))
        # pp.pprint(req._post)
        # print(req.POST, type(req.POST))
        form = UserForm(req.POST)
        if form.is_valid(): 
            print('form is valid')
            form_dict['data'] = form.cleaned_data


    return render(req, 'first_app/form_page.html', context = form_dict)

def user_form_page(req): 
    form = UserModelForm()
    form_dict = {
        'form': form,
        'data': {}
    }

    if req.method == 'POST': 
        form = UserModelForm(req.POST)
        if form.is_valid(): 
            new_form = form.save()
            form_dict['data'] = form.cleaned_data
            return first_app_index(req)
        else: 
            print('Form not valid')

    
    return render(req, 'first_app/user_form_page.html', context=form_dict)

def user_register(req):
    form_user = UserModelForm() 
    form_user_profile = UserProfileInfoForm()

    if req.method == 'POST': 
        print(req.POST)
        form_user = UserModelForm(req.POST) 
        form_user_profile = UserProfileInfoForm(req.POST)
        if form_user.is_valid() and form_user_profile.is_valid(): 
            # stuck in here for 3 hours because it's set_password() first and then,
            # save() to push to database, not save before set_password()
            # it's udemy's fault
            new_user = form_user.save(commit=False)
            new_user.set_password(new_user.password)
            new_user.save()
            new_user_profile = form_user_profile.save(commit=False)
            new_user_profile.user = new_user

            if 'picture' in req.FILES: 
                print(req.FILES)
                new_user_profile.picture = req.FILES['picture']
                new_user_profile.save()
                print(new_user_profile)
                return first_app_index(req)
            else:
                print('picture not uploaded')
        else: 
            print('Form not valid')
    
    return render(req, 'first_app/user_register.html', context={'form_user': form_user, 'form_user_profile': form_user_profile})

def user_login(req): 
    form = LoginForm()
    logged_in = False

    if req.method == 'POST': 
        form = LoginForm(req.POST)
        if form.is_valid(): 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user: 
                if user.is_active: 
                    login(req, user)
                    print('username: {} \t password: {} has logged in'.format(username, password))
                    return HttpResponseRedirect(reverse('index'))
                else: 
                    print('username: {} \t password: {} wants to logged in but inactive'.format(username, password))
                    return HttpResponse("ACCOUNT NOT ACTIVE")
            else: 
                print('login failed')
                print('username: {} \t password: {}'.format(username, password))
                return HttpResponse("Login failed")
        else: 
            print('Form not valid')
    return render(req, 'first_app/user_login.html', context={'form': form})

@login_required
def user_logout(req): 
    logout(req)
    return HttpResponseRedirect(reverse('index'))
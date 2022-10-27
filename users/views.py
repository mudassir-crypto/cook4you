from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

#from cook4you.settings import EMAIL_HOST_USER
from recipes.models import Recipe
from recipes.views import recipes
from .forms import CustomUserCreationForm, ProfileForm, ExperienceForm, EducationForm, MessageForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from .utils import paginationProfiles, searchProfiles
#from django.core.mail import send_mail


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('profiles')
        
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # send_mail(
            #     'Cook4You',
            #     'Here is the message.',
            #     EMAIL_HOST_USER,
            #     [user.email],
            #     fail_silently=False,
            # )
            #return redirect(request.GET['next'] if 'next' in request.GET else 'user-account')
            return redirect('user-account')
        else:
            messages.error(request, "Username OR Password is incorrect")

    context = {}
    return render(request, 'users/login.html', context)

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    messages.info(request, "User is successfully logged out!")
    return redirect('login')

def registerUser(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password1']
        
        message = 'Your Login Credential\n\nUsername: {}\nPassword: {}'.format(username, password)
        try:
            if form.is_valid:
                user = form.save()
                login(request, user)
                subject = 'You have successfully registered at Cook4You'
                
                # send_mail(
                #     subject,
                #     message,
                #     EMAIL_HOST_USER,
                #     [user.email],
                #     fail_silently=False,
                # )
                return redirect('edit-account')
               
            else:
                print("An error has occured during registration")
        except:
            print("An error has occured during registration process")

    context = {"form": form}
    return render(request, 'users/signup.html', context)

def profiles(request):
    profiles, search_query = searchProfiles(request)

    custom_range, profiles = paginationProfiles(request, profiles, 6)
    
    context = {'profiles': profiles, 'custom_range': custom_range, 'search_query':search_query}
    return render(request, 'users/profiles.html', context)

def top10(request):
    recipes = Recipe.objects.order_by('-vote_total')[:10]
    
    context = {'recipes': recipes}
    return render(request, 'users/top10.html', context)

def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    recipes = profile.recipe_set.all()
    context = {'profile': profile, 'recipes': recipes}
    return render(request, 'users/profile.html', context)

@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    
    experiences = profile.experience_set.all()
    educations = profile.education_set.all()
    recipes = profile.recipe_set.all()
    context = {"profile": profile, 'recipes': recipes, 'experiences': experiences, 'educations': educations}
    return render(request, 'users/account.html', context)

@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        
        if form.is_valid():
            form.save()
            return redirect('user-account')
    context = {"form": form}
    return render(request, 'users/profile_form.html', context)

@login_required(login_url='login')
def createExperience(request):
    profile = request.user.profile
    form = ExperienceForm()

    if request.method == 'POST':
        
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.owner = profile
            experience.save() 
            return redirect('user-account')
        else:
            print('error') 
    context = {'form': form}
    return render(request, 'users/profile_form.html', context)

@login_required(login_url='login')
def updateExperience(request, pk):
    profile = request.user.profile
    experience = profile.experience_set.get(id=pk)
    form = ExperienceForm(instance=experience)

    if request.method == 'POST':
        
        form = ExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.owner = profile
            experience.save() 
            return redirect('user-account')
        else:
            print('error') 
    context = {'form': form}
    return render(request, 'users/profile_form.html', context)

@login_required(login_url='login')
def deleteExperience(request, pk):
    profile = request.user.profile
    experience = profile.experience_set.get(id=pk)
    if request.method == 'POST':
        experience.delete()
        return redirect('user-account')
    context = {'recipe': experience}
    return render(request, 'recipes/delete.html', context)

@login_required(login_url='login')
def createEducation(request):
    profile = request.user.profile
    form = EducationForm()

    if request.method == 'POST':
        
        form = EducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.owner = profile
            education.save() 
            return redirect('user-account')
        else:
            print('error') 
    context = {'form': form}
    return render(request, 'users/profile_form.html', context)

@login_required(login_url='login')
def updateEducation(request, pk):
    profile = request.user.profile
    education = profile.education_set.get(id=pk)
    form = EducationForm(instance=education)

    if request.method == 'POST':
        
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            education = form.save(commit=False)
            education.owner = profile
            education.save() 
            return redirect('user-account')
        else:
            print('error') 
    context = {'form': form}
    return render(request, 'users/profile_form.html', context)

@login_required(login_url='login')
def deleteEducation(request, pk):
    profile = request.user.profile
    education = profile.education_set.get(id=pk)
    if request.method == 'POST':
        education.delete()
        return redirect('user-account')
    context = {'recipe': education}
    return render(request, 'recipes/delete.html', context)

@login_required(login_url='login')
def inbox(request):
    profile = request.user.profile
    messageRequests = profile.recipient.all()
    unread_messagesCount = messageRequests.filter(is_read=False).count()
    context = {"unread_messagesCount": unread_messagesCount, "messageRequests": messageRequests}
    return render(request, 'users/inbox.html', context)

@login_required(login_url='login')
def viewMessage(request, pk):
    profile = request.user.profile
    message = profile.recipient.get(id=pk)
    if message.is_read == False:
        message.is_read = True
        message.save()
    context = {"message": message}
    return render(request, 'users/message.html', context)

def sendMessage(request, pk):
    recipient = Profile.objects.get(id=pk)
    form = MessageForm()

    try:
        sender = request.user.profile
    except:
        sender = None
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.reciever = recipient

            if sender:
                message.name = sender.name
                message.email = sender.email
            message.save()
            subject = '{} just messaged you'.format(str(sender.name).split(' ')[0].capitalize())
            # send_mail(
            #     subject,
            #     'One New Message awaits your response',
            #     EMAIL_HOST_USER,
            #     [recipient.email],
            #     fail_silently=False,
            # )
            messages.success(request, "Your message is successfully sent!")
            return redirect('profile', pk=recipient.id)
    context = {"form": form, "recipient": recipient}
    return render(request, 'users/message_form.html', context)
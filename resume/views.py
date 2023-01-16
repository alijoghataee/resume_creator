from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *


@login_required
def resume_creator(request):
    if request.method == 'POST':
        resume_form = ResumeForm(request.POST)
        if resume_form.is_valid():
            second_resume_form = resume_form.save(commit=False)
            second_resume_form.user = request.user
            second_resume_form.save()
            return redirect('experience')

    else:
        resume_form = ResumeForm()

    return render(request, 'resume/resume_creator.html', context={'form': resume_form})


def experience(request):
    if request.method == 'POST':
        experience_form = ExperienceForm(request.POST)
        if experience_form.is_valid():
            second_experience_form = experience_form.save(commit=False)
            second_experience_form.user = request.user
            second_experience_form.save()
            experience_form = ExperienceForm()
            messages.success(request, 'you want add more?')
    else:
        experience_form = ExperienceForm()

    return render(request, 'resume/experience.html', context={'form': experience_form})


def project(request):
    if request.method == 'POST':
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            second_project_form = project_form.save(commit=False)
            second_project_form.user = request.user
            second_project_form.save()
            project_form = ProjectForm()
            messages.success(request, 'you want add more?')
    else:
        project_form = ProjectForm()

    return render(request, 'resume/project.html', context={'form': project_form})


def social_media(request):
    if request.method == 'POST':
        social_media_form = SocialMediaForm(request.POST)
        if social_media_form.is_valid():
            second_social_media_form = social_media_form.save(commit=False)
            second_social_media_form.user = request.user
            second_social_media_form.save()
            social_media_form = SocialMediaForm()
            messages.success(request, 'you want add more?')
    else:
        social_media_form = SocialMediaForm()

    return render(request, 'resume/social_media.html', context={'form': social_media_form})

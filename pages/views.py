from abc import ABC

from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from resume.models import *


@login_required
def resume_list_view(request):
    resume_list = Resume.objects.filter(user=request.user)
    return render(request, 'pages/resume_list.html', context={'resume': resume_list})


@login_required
def resume_detail_view(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    experience = Experience.objects.filter(user=request.user)
    project = Project.objects.filter(user=request.user)
    social_media = SocialMedia.objects.filter(user=request.user)

    return render(request, 'pages/resume_detail.html', context={
        'resume': resume,
        'experiences': experience,
        'projects': project,
        'social_medias': social_media,
    })

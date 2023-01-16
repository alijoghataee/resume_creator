from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Experience(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_of = models.DateField()
    end = models.DateField()


class Project(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    project_name = models.CharField(max_length=50)
    summary_about_project = models.CharField(max_length=500)
    link = models.URLField()


class SocialMedia(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    link = models.URLField()


class Resume(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, unique=True)
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=200)
    number = models.CharField(max_length=11, blank=True)
    email = models.EmailField(unique=True)
    profile = models.CharField(max_length=400)
    skills = models.TextField()
    hobby = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('resume_detail', args=[self.id])

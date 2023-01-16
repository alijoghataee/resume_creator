from django.forms import ModelForm

from .models import Resume, Experience, Project, SocialMedia


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = ('name', 'profession', 'number', 'email', 'profile', 'skills', 'hobby', )


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ('company_name', 'position', 'start_of', 'end', )


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('project_name', 'summary_about_project', 'link', )


class SocialMediaForm(ModelForm):
    class Meta:
        model = SocialMedia
        fields = ('name', 'link', )

from django.contrib import admin

from .models import Resume, Experience, Project, SocialMedia


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'profession', )


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'position', )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', )


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('name', )

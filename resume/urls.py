from django.urls import path

from .views import *


urlpatterns = [
    path('create/', resume_creator, name='create_resume'),
    path('experience/', experience, name='experience'),
    path('project/', project, name='project'),
    path('social_media/', social_media, name='social_media'),

]

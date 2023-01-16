from django.urls import path

from .views import resume_list_view, resume_detail_view


urlpatterns = [
    path('', resume_list_view, name='home'),
    path('resume_detail/<int:pk>/', resume_detail_view, name='resume_detail'),
]

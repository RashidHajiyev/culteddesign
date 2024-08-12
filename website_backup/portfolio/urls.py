from django.urls import path
from . import views
from django.shortcuts import redirect


urlpatterns = [
    path('', views.home, name='home'),
    path('home/', lambda request: redirect('')),

    path('projects/', views.projects, name='projects'),
    path('portfolio/', views.portfolio_view, name='portfolio'),
]

# path('feedback/', views.feedback_view, name='feedback'),

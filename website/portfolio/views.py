# portfolio/views.py
from django.shortcuts import render, redirect
from .models import Project, UserDescription, Portfolio
from .forms import CustomerForm
from django.contrib import messages


def home(request): #home page with description
    user_descriptions = UserDescription.objects.all()
    return render(request, 'portfolio/index.html', {'user_descriptions': user_descriptions})


def projects(request):  #projects view
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})
#    return render(request, 'portfolio/projects.html')


def portfolio_view(request): # protfolio view
    portfolio = Portfolio.objects.all()
    return render(request, 'portfolio/portfolio.html', {'portfolio': portfolio})


def contact_form(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submitted successfully!')
            return redirect('success')  # Redirect to a success page or another view
        else:
            messages.error(request, 'Form submission failed. Please check the input.')
    else:
        form = CustomerForm()
    return render(request, 'contact_form.html', {'form': form})


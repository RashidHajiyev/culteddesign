# portfolio/views.py
from django.shortcuts import render, redirect
from .models import Project, UserDescription, Portfolio
from .forms import ContactForm
from django.contrib import messages


def home(request): #home page with description
    if request.method == 'GET':
        user_descriptions = UserDescription.objects.all()
        return render(request, 'portfolio/index.html', {'user_descriptions': user_descriptions})

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the Customer model
            messages.success(request, "Your message has been sent successfully!")
            return redirect('home')  # Redirect back to the contact form page or another page
        else:
            messages.error(request, "There was an error in your submission.")
    else:
        form = ContactForm()

    return render(request, 'portfolio/index.html', {'form': form})


def projects(request):
    if request.method == 'GET':
        projects = Project.objects.all()
        return render(request, 'portfolio/projects.html', {'projects': projects})

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the Customer model
            messages.success(request, "Your message has been sent successfully!")
            return redirect('projects')  # Redirect back to the contact form page or another page
        else:
            messages.error(request, "There was an error in your submission.")
    else:
        form = ContactForm()

    return render(request, 'portfolio/projects.html', {'form': form})


def portfolio(request): # portfolio view
    if request.method == 'GET':
        portfolio = Portfolio.objects.all()
        return render(request, 'portfolio/portfolio.html', {'portfolio': portfolio})

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the Customer model
            messages.success(request, "Your message has been sent successfully!")
            return redirect('portfolio')  # Redirect back to the contact form page or another page
        else:
            messages.error(request, "There was an error in your submission.")
    else:
        form = ContactForm()

    return render(request, 'portfolio/portfolio.html', {'form': form})

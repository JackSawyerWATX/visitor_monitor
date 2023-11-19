# visitor_counter/views.py
from django.shortcuts import render, redirect
from .models import Visitor

def home(request):
    # Retrieve the visitor count from the database
    visitor_count = Visitor.objects.first().count
    return render(request, 'home.html', {'visitor_count': visitor_count})

def visitor_count(request):
    # Retrieve the visitor count from the database
    visitor_count = Visitor.objects.first().count
    return render(request, 'visitor_counter/home.html', {'visitor_count': visitor_count})

def reset_count(request):
    if request.method == 'POST':
        # Reset the visitor count
        Visitor.objects.update(count=0)
        return redirect('home')

#     # If it's not a POST request, render the visitor_count page
#     visitor_count = Visitor.objects.first().count
#     return render(request, 'visitor_counter/home.html', {'visitor_count': visitor_count})

# def reset_count(request):
#     if request.method == 'POST':
#         # Reset the visitor count
#         Visitor.objects.update(count = 0)
#         return redirect('home')  # Redirect to the home view after resetting the count

# def reset_count(request):
#     if request.method == 'POST':
#         # Reset the visitor count
#         visitor_instance = Visitor.objects.first()
#         if visitor_instance:
#             visitor_instance.count = 0
#             visitor_instance.save()
#         return redirect('home')  # Redirect to the home view after resetting the count

# def reset_count(request):
#     if request.method == 'POST':
#         # Reset the visitor count
#         visitor_instance = Visitor.objects.first()
#         visitor_instance.count = 0
#         visitor_instance.save()
#         return redirect('home')

#     # If it's not a POST request, render the visitor_count page
#     visitor_count = Visitor.objects.first().count
#     return render(request, 'visitor_counter/home.html', {'visitor_count': visitor_count})

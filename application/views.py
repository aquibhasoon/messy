from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'application/home.html', {})

def profile(request):
	return render(request, 'application/profile.html', {})
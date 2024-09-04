from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    logout(request)  # Log out the user
    return redirect('home')  # Redirect to the home page

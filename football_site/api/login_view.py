from django.contrib.auth import views as auth_views
from django.shortcuts import render

class CustomLoginView(auth_views.LoginView):
    template_name = 'registration/login.html'  # Update with your template path

    def form_valid(self, form):
        # Call the parent class's form_valid method to log in the user
        response = super().form_valid(form)  # Store the response
        return response  # Return the response

    def get_success_url(self):
        # Get the 'next' parameter from the request, default to home if not provided
        return self.request.GET.get('next', '/')

    def form_invalid(self, form):
        # Pass the error messages to the template context
        return render(self.request, self.template_name, {'form': form, 'error': 'Invalid username or password.'})

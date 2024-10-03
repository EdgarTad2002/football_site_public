from django.contrib.auth import views as auth_views
from django.shortcuts import render

class CustomLoginView(auth_views.LoginView):
    template_name = 'registration/login.html'  # Update with your template path

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        # Pass the error messages to the template context
        return render(self.request, self.template_name, {'form': form, 'error': 'Invalid username or password.'})

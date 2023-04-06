from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import View, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
# Create your views here.

class HomeView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'accounts/home.html')

class PasswordChangeView(PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('home-page')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            # messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'accounts/profile.html', context)


class RegisterView(FormView):
	form_class = UserRegistrationForm
	template_name = 'accounts/signup.html'

	def form_valid(self, form):
		request = self.request
		user = form.save()
		return redirect('home-page')


class SigninView(LoginView):
	template_name = 'accounts/signin.html'

	def form_Valid(self, request, *args, **kwargs):
		request = self.request
		return redirect('home-page')

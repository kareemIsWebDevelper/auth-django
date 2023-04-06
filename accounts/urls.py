from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views
# Map your paths here

urlpatterns = [
	path('', views.HomeView.as_view(), name='home-page'),
	path('profile/', views.profile, name='profile'),
	path('signup/', views.RegisterView.as_view(), name='signup'),
	path('signin/', views.SigninView.as_view(), name='signin'),
	path('signout/', auth_views.LogoutView.as_view(template_name='accounts/signout.html'), name='signout'),
	path('password-change/', views.PasswordChangeView.as_view(), name='password_change'),
]
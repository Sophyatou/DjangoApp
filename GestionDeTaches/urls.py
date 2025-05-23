from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from taches.views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='taches/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', include('taches.urls')),
]
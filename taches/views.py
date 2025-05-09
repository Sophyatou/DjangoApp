from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Tache
from .forms import TacheForm, SignUpForm

class TacheListView(LoginRequiredMixin, ListView):
    model = Tache
    template_name = 'taches/tache_list.html'

    def get_queryset(self):
        return Tache.objects.filter(user=self.request.user).order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['completed_count'] = Tache.objects.filter(user=self.request.user, completed=True).count()
        context['pending_count'] = Tache.objects.filter(user=self.request.user, completed=False).count()
        return context
        
       
class TacheCreateView(LoginRequiredMixin, CreateView):
    model = Tache
    form_class = TacheForm
    template_name = 'taches/tache_form.html'
    success_url = reverse_lazy('tache_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TacheUpdateView(LoginRequiredMixin, UpdateView):
    model = Tache
    form_class = TacheForm
    template_name = 'taches/tache_form.html'
    success_url = reverse_lazy('tache_list')

class TacheDeleteView(LoginRequiredMixin, DeleteView):
    model = Tache
    template_name = 'taches/tache_confirm_delete.html'
    success_url = reverse_lazy('tache_list')

class SignUpView(FormView):
    template_name = 'taches/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('tache_list')

    def form_valid(self, form):
        user = form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)
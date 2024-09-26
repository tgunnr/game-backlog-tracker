from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .models import Game
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def game_index(request):
  games = Game.objects.filter(user=request.user)
  return render(request, 'games/index.html', { 'games': games })

@login_required
def game_detail(request, game_id):
  game = Game.objects.get(id=game_id)
  return render(request, 'games/detail.html', {
    'game': game,
  })

class GameCreate(LoginRequiredMixin, CreateView):
  model = Game
  fields = ['name', 'platform', 'genre', 'status']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  
class GameUpdate(LoginRequiredMixin, UpdateView):
  model = Game
  fields = ['name', 'platform', 'genre', 'status']

class GameDelete(LoginRequiredMixin, DeleteView):
  model = Game
  success_url = '/games/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('game-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  return render(request, 'signup.html', {
    'form': form,
    'error_message': error_message
  })
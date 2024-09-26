from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

GENRES = (
  ('A', 'Action/ Adventure'),
  ('F', 'Family'),
  ('FI', 'Fighting'),
  ('LS', 'Life Sim'),
  ('MM', 'MMO/ MOBA'),
  ('P', 'Platformer'),
  ('R', 'Racing'),
  ('RPG', 'RPG'),
  ('S', 'Shooter'),
  ('SP', 'Sports'),
  ('ST', 'Stealth'),
)

STATUSES = (
  ('U', 'Unstarted'),
  ('P', 'Playing'),
  ('B', 'Taking a Break'),
  ('F', 'Finished'),
)

# Create your models here.

class Game(models.Model):
  name = models.CharField(max_length=50)
  platform = models.CharField(max_length=50)
  genre = models.CharField(
    max_length=3,
    choices=GENRES,
    default=GENRES[0][0]
  )
  status = models.CharField(
    max_length=1,
    choices=STATUSES,
    default=STATUSES[0][0]
  )
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('game-detail', kwargs={'game_id': self.id})

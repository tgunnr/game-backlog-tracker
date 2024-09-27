from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('games/', views.game_index, name='game-index'),
  path('games/<int:game_id>/', views.game_detail, name='game-detail'),
  path('games/create', views.GameCreate.as_view(), name='game-create'),
  path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='game-update'),
  path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='game-delete'),
  path('accounts/signup/', views.signup, name='signup')
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.urls import path
from .views import MoviesView, PlanetsView, FavoritesView

urlpatterns = [
    path('movies/', MoviesView.as_view()),
    path('planets/', PlanetsView.as_view()),
    path('<str:obj>/<int:pk>/favorite', FavoritesView.as_view({'put': 'put'})),
]

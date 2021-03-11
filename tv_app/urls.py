from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.addShow),
    path('shows/processNew', views.processNew),
    path('shows/delete/<int:showId>', views.deleteShow),
    path('shows/<int:showId>', views.showDisplay),
    path('shows/process/<int:showId>', views.showProcess),
    path('shows/update/<int:showId>', views.updateShow),
    path('shows/updateNew/<int:showId>', views.updateNew),

]

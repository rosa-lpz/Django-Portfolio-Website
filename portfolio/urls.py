from django.urls import path 
from .views import render_projects
app_name = 'portfolio'

urlpatterns = [
    # Render all projects in initial page (/portfolio)
    path('', render_projects, name='projects')


]
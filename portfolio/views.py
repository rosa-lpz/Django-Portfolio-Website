from django.shortcuts import render
from .models import Project

# Render all projects in portfolio page
def render_projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

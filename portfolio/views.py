from django.shortcuts import render
from .models import Proj
# Create your views here.
def home(request):
	projects = Proj.objects.all()
	return render(request, 'portfolio/home.html', {'projects':projects})
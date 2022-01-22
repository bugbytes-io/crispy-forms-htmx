from django.shortcuts import render

from core.forms import UniversityForm

# Create your views here.
def index(request):
    context = {'form': UniversityForm()}
    return render(request, 'index.html', context)
from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import csrf
from crispy_forms.utils import render_crispy_form
from django.contrib.auth import login

from core.forms import UniversityForm

# Create your views here.
def index(request):
    if request.method == 'GET':
        context = {'form': UniversityForm()}
        return render(request, 'index.html', context)
    
    elif request.method == 'POST':
        form = UniversityForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            template = render(request, 'profile.html')
            template['Hx-Push'] = '/profile/'
            return template

        ctx = {}
        ctx.update(csrf(request))
        form_html = render_crispy_form(form, context=ctx)
        return HttpResponse(form_html)

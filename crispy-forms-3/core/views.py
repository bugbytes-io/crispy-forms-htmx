from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import csrf
from crispy_forms.utils import render_crispy_form
from crispy_forms.templatetags.crispy_forms_filters import as_crispy_field

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


def check_username(request):
    form = UniversityForm(request.GET)
    context = {
        'field': as_crispy_field(form['username']),
        'valid': len(form['username'].errors) == 0
    }
    return render(request, 'partials/field.html', context)

def check_subject(request):
    form = UniversityForm(request.GET)
    context = {
        'field': as_crispy_field(form['subject']),
        'valid': len(form['subject'].errors) == 0
    }
    return render(request, 'partials/field.html', context)
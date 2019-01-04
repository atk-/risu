from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .forms import DesignerMainForm, DesignerGridForm

def _index(request):
    return HttpResponse('''<h1>ooh, welcome, you astonishing sod ape</h1>
                        <h3>then welcome in <b>jam</strong></b>''')

def index(request):
    template = loader.get_template('designer/index.html')
    return HttpResponse(template.render({}, request))


def designer(request):
    form = DesignerGridForm()
    return render(request, 'designer/designer.html', {'form': form})


def collect_words(request):
    print('>', request.body, dir(request.body))
    return JsonResponse({'foo': 'bar',})

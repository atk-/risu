from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import DesignerMainForm

def _index(request):
    return HttpResponse('''<h1>ooh, welcome, you astonishing sod ape</h1>
                        <h3>then welcome in <b>jam</strong></b>''')

def index(request):
    template = loader.get_template('designer/index.html')
    return HttpResponse(template.render({}, request))


def designer(request):
    form = DesignerMainForm()
    #template = loader.get_template('designer/designer.html')
    #return HttpResponse(template.render({}, request))
    return render(request, 'designer/designer.html', {'form': form, 'width': 34 * 12})

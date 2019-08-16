from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.generic.edit import FormView

from .forms import DesignerMainForm, DesignerGridForm

def _index(request):
    return HttpResponse('''<h1>ooh, welcome, you astonishing sod ape</h1>
                        <h3>then welcome in <b>jam</strong></b>''')

def index(request):
    template = loader.get_template('designer/index.html')
    return HttpResponse(template.render({}, request))


def designer(request):
    form = DesignerGridForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        print('!!', cd)
    else:
        print('invalid form!')
    return render(request, 'designer/designer.html', {'form': form})


def collect_words(request):
    print('>', request.body, dir(request.body))
    return JsonResponse({'foo': 'bar',})


class MainView(FormView):
    form_class = DesignerGridForm
    template_name = 'designer/designer.html'

    def get(self, request, *args, **kwargs):
        print("MainView GET", args, kwargs)
        return render(request, self.template_name, {})

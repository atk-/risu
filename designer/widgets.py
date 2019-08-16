import django.forms
import django.forms.widgets


class GridWidget(django.forms.MultiWidget):
    def __init__(self, **kwargs):
        self.rows = kwargs['rows']
        self.columns = kwargs['columns']

        self.widgets = [django.forms.TextInput(attrs={'class': 'cword-cell', 'maxlength': 1})
                        for i in range(self.rows) for j in range(self.columns)]
        super().__init__(self.widgets) #, **kwargs)

    def decompress(self, value):
        print('> decompress')


class GridField(django.forms.MultiValueField):
    #widget = GridWidget

    def __init__(self, *args, **kwargs):
        fields = [django.forms.CharField(max_length=1, required=False, label='z')
                  for i in range(kwargs['columns'] * kwargs['rows'])]
        self.widget = GridWidget(**kwargs)
        super(GridField, self).__init__(fields=fields, require_all_fields=False, *args)

    def compress(self, values):
        return ''.join(values)

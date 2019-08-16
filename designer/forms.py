from django import forms
from designer.widgets import GridWidget, GridField

ACROSS = 0
DOWN = 1


class DesignerMainForm(forms.Form):
    columns = forms.IntegerField()
    rows = forms.IntegerField()


class DesignerGridForm(forms.Form):
    class Meta:
        fields = ('grid',)
        widgets = {'grid': GridWidget}

    rows = 5
    columns = 8

    direction = forms.ChoiceField(choices=[['0', 'Across'], ['1', 'Down']])

    grid = GridField(rows=rows, columns=columns)
    griddata = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.griddata = [[None for y in range(self.columns)] for x in range(self.rows)]

    def is_valid(self):
        self.cleaned_data = self.data
        self.griddata = [[self.data['grid_%d' % d] for d in range(n * self.rows, n * self.rows + self.columns)]
                         for n in range(self.rows)]
        print('#', self.griddata)
        return True

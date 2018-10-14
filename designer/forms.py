from django import forms

class DesignerMainForm(forms.Form):
    columns = 12
    rows = 8
    foo = 'bar'
    text = forms.CharField(label='fobar', max_length=30)
    grid = [forms.CharField(max_length=1) for i in range(rows*columns)]
    grid2 = [[forms.CharField(max_length=1) for i in range(12)] for j in range(rows)]

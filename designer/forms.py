from django import forms

class DesignerMainForm(forms.Form):
    columns = forms.IntegerField() 
    rows = forms.IntegerField()


class DesignerGridForm(forms.Form):
    rows = 7
    columns = 10
    grid2 = []
    for i in range(rows):
        grid2.append([forms.CharField(max_length=1) for i in range(columns)])

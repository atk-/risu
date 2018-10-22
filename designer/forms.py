from django import forms

ACROSS = 0
DOWN = 1


class DesignerMainForm(forms.Form):
    columns = forms.IntegerField()
    rows = forms.IntegerField()


class DesignerGridForm(forms.Form):
    rows = 7
    columns = 10

    direction = forms.ChoiceField(choices=[['0', 'Across'], ['1', 'Down']])

    grid = []
    for i in range(rows):
        grid.append([forms.CharField(max_length=1) for i in range(columns)])

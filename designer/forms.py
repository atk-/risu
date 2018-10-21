from django import forms

ACROSS = (1, 0)
DOWN = (0, 1)


class DesignerMainForm(forms.Form):
    columns = forms.IntegerField()
    rows = forms.IntegerField()


class DesignerGridForm(forms.Form):
    rows = 7
    columns = 10

    direction = ACROSS

    grid = []
    for i in range(rows):
        grid.append([forms.CharField(max_length=1) for i in range(columns)])

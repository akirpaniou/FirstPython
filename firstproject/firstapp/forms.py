from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label="Enter ur name", initial="undefined")
    age = forms.IntegerField(help_text="enter ur age")
    age2 = forms.IntegerField()
    comment = forms.CharField(required=False, label="Ur comment", widget=forms.Textarea)
    weight = forms.DecimalField(min_value=3, max_value=200, decimal_places=2)
    field_order = ["age", "name"]

class LesOne(forms.Form):
    check = forms.BooleanField(required=False)

class LesTwo(forms.Form):
    yn = forms.NullBooleanField(required=False)

class LesTh(forms.Form):
    text = forms.FileField(required=False)

class LesF(forms.Form):
    choice = forms.ChoiceField(required=False, choices=((1, "lol"), (2, "test"), (3, "good")))


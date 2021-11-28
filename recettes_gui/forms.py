from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(label='recherche', max_length=100)
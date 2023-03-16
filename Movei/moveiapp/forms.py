from django import forms
from .models import movei
# for edit
class moveiform(forms.ModelForm):
    class Meta:
        model=movei
        fields=['name','desc','year','img']

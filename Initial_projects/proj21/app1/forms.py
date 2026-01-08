from app1.models import EmpModel
from django import forms

class Empform(forms.ModelForm):
    class Meta:
        model=EmpModel
        fields=['empno','empname','jobs','salary']



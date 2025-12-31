from django import forms
from empapp.models import EmpModel

class Empform(forms.ModelForm):
    class Meta:
        model=EmpModel
        fields=['empno','empname','empjob','empsal']

from django.forms import ModelForm
from app1.models import EmpModel

class Empform(ModelForm):
    class Meta:
        model=EmpModel
        fields=['empno','empname','job','salary']

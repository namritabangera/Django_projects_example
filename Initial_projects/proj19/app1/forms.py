from django import forms
from django.core.validators import *
from app1.models import Customer

def course_validator(c):
    if c not in ["python","java","c++"]:
        raise forms.ValidationError("Course must be python,java,c++")
    else:
        return c
    
def uppercase_validator(n):
    if not n.isupper():
        raise forms.ValidationError('Name must be uppercase')    
    else:
        return n
    


class EmailForm(forms.Form):

    name=forms.CharField(validators=[MinLengthValidator(1),MaxLengthValidator(20),uppercase_validator])
    age=forms.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)])
    email=forms.CharField(validators=[EmailValidator()])
    doj=forms.CharField(validators=[RegexValidator(r'[0-9]{2}/[0-9]{2}/[0-9]{4}')])
    course=forms.CharField(validators=[course_validator])
    fee=forms.IntegerField()



    def clean_fee(self):
        d=super().clean()
        print(d)
        if d['course']=='python' and d['fee']!=4000:
            raise forms.ValidationError('Fee must be 4000')
        elif d['course']=='java' and d['fee']!=2000:
            raise forms.ValidationError('Fee must be 2000')
        elif d['course']=='mysql' and d['fee']!=0:
            raise forms.ValidationError('Fee must be 0')
        else:
            return d

class CustomerForm(forms.ModelForm):
    cname=forms.CharField(validators=[uppercase_validator])
    class Meta:
        model=Customer
        fields=['custid','cname','address']





    




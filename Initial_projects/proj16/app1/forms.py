from django import forms
class StudentForm(forms.Form):
    rollno=forms.IntegerField()
    name=forms.CharField(max_length=20)
    course=forms.CharField(max_length=20)


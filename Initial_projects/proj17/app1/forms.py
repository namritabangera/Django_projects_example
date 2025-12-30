from django import forms

class RegisterForm(forms.Form):
    uname=forms.CharField(max_length=12)
    password=forms.CharField(max_length=8,widget=forms.PasswordInput())
    cpassword=forms.CharField(max_length=8,widget=forms.PasswordInput())

    def clean_cpassword(self):
        d=super().clean()
        if(d['password']==d['cpassword']):
            return d
        else:
            print("Password dont match")
            raise forms.ValidationError("Password doesnt not match with Confirm")




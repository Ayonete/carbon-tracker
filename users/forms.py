from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

class UserSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, help_text=None)

    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(UserSignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None  

    def save(self, commit=True):
        user = super(UserSignUpForm, self).save(commit=False)
        raw_password = self.cleaned_data['password']
        user.set_password(raw_password)
        if commit:
            user.save()
        return user

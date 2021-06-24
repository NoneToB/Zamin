from django import forms
from .models import Profile


class DateInput(forms.DateInput):
    input_type = 'date'


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = Profile
        widgets = {
            'date_of_birth': DateInput
        }
        labels = {
            'date_of_birth': '',
            'profile_pic': '',
        }
        fields = ('username', 'first_name', 'date_of_birth', 'email', 'school')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'signup__input'
            visible.field.widget.attrs['required'] = 'true'

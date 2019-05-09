import json

from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User
from .authyUtils import check_verification
from django.core.exceptions import ValidationError

from .widgets import DateOfBirthInput, PasswordFieldInput, OperatorDropDown


class RegisterLoginForm(forms.Form):
    action = forms.CharField(max_length=60, widget=forms.HiddenInput())


class SignUpForm(forms.ModelForm):
    # url = settings.BASE_DIR + static('js/country.json')
    # print(url)
    # for d in json.loads(
    #         open(url).read()):

    # country_code = forms.ChoiceField(choices=[(d['dial_code'],str(d['dial_code'])) for d in json.loads(
    #                         open(url).read()) if d['dial_code'] is not None and d['dial_code'] != ""])

    # print("printing country code")
    action = forms.CharField(max_length=60, widget=forms.HiddenInput())
    message_id = forms.CharField(max_length=60, widget=forms.HiddenInput())

    otp = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        widget=PasswordFieldInput()
    )
    password2 = forms.CharField(
        widget=PasswordFieldInput()
    )

    class Meta:
        model = User
        fields = ('name', 'gender', 'date_of_birth', 'email', 'mobile_operator', 'mobile_number', 'otp')
        widgets = {

            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': DateOfBirthInput(),
            'mobile_number' : forms.TextInput(attrs={'class': 'form-control'}),
             


        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1!= password2:
            raise forms.ValidationError("Password don't match")
        return password2

    def clean_otp(self):
        otp = self.cleaned_data.get('otp')
        return otp

    def save(self, commit=True):
        user = super(SignUpForm,self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

        # verification = check_verification()
        #
        # if not verification.ok():
        #return True

            #self.add_error("otp","otp verification failed")


class LoginForm(RegisterLoginForm):
    mobile_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        widget=PasswordFieldInput()
    )





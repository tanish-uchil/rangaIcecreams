from django import forms
from accounts.models import Customer
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm


class UpdateUserForm(UserChangeForm):
    class Meta:
        model = Customer
        fields = ['username','email','phone_number','address']

        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Username"
        })
        self.fields["email"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Email"
        })
        self.fields["phone_number"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Phone Number"
        })
        self.fields["address"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Address"
        })

class SignUpForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['username', 'password1', 'password2', 'email', 'phone_number', 'address']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Password"
        })
        self.fields["password2"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Confirm Password"
        })
        self.fields["username"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Username"
        })
        self.fields["email"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Email"
        })
        self.fields["phone_number"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Phone Number"
        })
        self.fields["address"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Address"
        })
        
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Password"
        })
        self.fields["username"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Username"
        })

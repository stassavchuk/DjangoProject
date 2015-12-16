from django import forms
from .models import SignUp

class ContactForm(forms.Form):
    full_name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField()

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     email_base, proveder = email.split("@")
    #     domain, extention = proveder.split(".")
    #     if extention != "edu":
    #         raise forms.ValidationError("Please use a correct university email")
    #     return email

class SignUpForm (forms.ModelForm):
    class Meta:
        model = SignUp
        # this is how you will see your signups data in what sequence
        fields = ['full_name', 'email']

    # Validation of email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, proveder = email.split("@")
        domain, extention = proveder.split(".")
        if extention != "edu":
            raise forms.ValidationError("Please use a correct university email")
        return email

    # Validation of full name
    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        # My code here
        return full_name
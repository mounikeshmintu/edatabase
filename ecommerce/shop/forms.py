from django import forms

class ContactForm(forms.Form):

    name= forms.CharField(widget= forms.TextInput(attrs={"class":'form-control','placeholder':'your name'}))
    email = forms.EmailField(widget= forms.EmailInput(attrs={'class':'form-control','placeholder':'your email please'}))
    text=forms.CharField(widget = forms.Textarea(attrs={"class":"form-control",'placeholder':"your text"}))


    def clean_email(self):

        email = self.cleaned_data.get("email")
        if not "gmail.com " in email:

           raise forms.ValidationError("your email should be gmail only ")
        return email
class LoginForm(forms.Form):
    username= forms.CharField()
    password= forms.CharField(widget = forms.PasswordInput)
class RegisterForm(forms.Form):
    username= forms.CharField()
    email = forms.EmailField()
    password= forms.CharField(widget = forms.PasswordInput)
    password2 = forms.CharField(widget = forms.PasswordInput)

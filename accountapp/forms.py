from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from accountapp.models import User


class AccountCreateForm(UserCreationForm):

    email = forms.CharField(label='이메일', widget=forms.TextInput(attrs={'placeholder' : 'example@email.com'}))
    password1 = forms.PasswordInput(attrs={'placeholder' : None})

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class AccountUpdateForm(AccountCreateForm):
    def __init__(self, *args, **kwargs):
        super(AccountUpdateForm, self).__init__(*args, **kwargs)

        self.fields['email'].disabled = True # username 비활성화


class UserCreationForm(forms.ModelForm):
   """A form for creating new users. Includes all the required
   fields, plus a repeated password."""
   password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
   password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

   class Meta:
       model = User
       fields = ('email',)

   def clean_password2(self):
       # Check that the two password entries match
       password1 = self.cleaned_data.get("password1")
       password2 = self.cleaned_data.get("password2")
       if password1 and password2 and password1 != password2:
           raise ValidationError("Passwords don't match")
       return password2

   def save(self, commit=True):
       # Save the provided password in hashed format
       user = super().save(commit=False)
       user.set_password(self.cleaned_data["password1"])
       if commit:
           user.save()
       return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'is_active', 'is_admin')
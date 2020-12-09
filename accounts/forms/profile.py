from django import forms

from accounts.models import UserProfile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', )

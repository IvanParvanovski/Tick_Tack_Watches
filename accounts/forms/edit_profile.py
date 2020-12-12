from django import forms
from django.contrib.auth.models import User


class ProfileEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    email = forms.CharField(max_length=150)
    phone_number = forms.CharField(max_length=150)
    profile_picture = forms.ImageField(max_length=150)

    class Meta:
        model = User
        fields = ('username', )


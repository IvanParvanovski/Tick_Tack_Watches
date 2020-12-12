from django.contrib.auth import logout, login, authenticate
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, UpdateView, DeleteView
from django.views.generic.base import View

from accounts.forms.edit_profile import ProfileEditForm
from accounts.forms.login import LoginForm
from accounts.forms.profile import ProfileForm

from django.contrib.auth.models import User
from django.views.generic import DetailView

from accounts.models import UserProfile


class Profile(DetailView):
    template_name = 'accounts/profile.html'
    model = User


class ProfileEdit(View):
    def get(self, req, pk):
        user = User.objects.get(pk=pk)
        form = ProfileEditForm(initial={
            'username': user.get_username(),
            'phone_number': user.userprofile.telephone_number,
            'email': user.userprofile.email,
            'profile_picture': user.userprofile.profile_picture
        })

        context = {
            'form': form,
        }
        return render(req, 'accounts/profile_edit.html', context=context)

    def post(self, req, pk):
        user = User.objects.get(pk=pk)
        form = ProfileEditForm(req.POST, req.FILES, instance=user)

        if form.is_valid():
            user.userprofile.email = form.cleaned_data['email']
            user.userprofile.profile_picture = form.cleaned_data['profile_picture']
            user.userprofile.telephone_number = form.cleaned_data['phone_number']
            user.userprofile.profile_picture = form.cleaned_data['profile_picture']
            form.save()
            user.userprofile.save()
            return redirect('profile', user.id)

        context = {
            'form': form
        }

        return render(req, 'accounts/profile_edit.html', context=context)


class UserSignUp(CreateView):
    form_class = ProfileForm
    template_name = 'accounts/sign_up.html'
    success_url = reverse_lazy('display watches')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for (_, field) in form.fields.items():
            field.widget.attrs['class'] = 'form-control'
        return form

    def form_valid(self, form):
        user = form.save(commit=False)
        userprofile = UserProfile(user=user,
                                  telephone_number=form.cleaned_data['phone_number'],
                                  email=form.cleaned_data['email'])
        user.save()
        userprofile.save()
        login(self.request, user)
        return redirect('home page')


class UserSignIn(FormView):
    template_name = 'accounts/sign_in.html'
    form_class = LoginForm

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for (_, field) in form.fields.items():
            field.widget.attrs['class'] = 'form-control'
        return form

    def form_valid(self, form):
        user = authenticate(**form.cleaned_data)
        if user:
            login(self.request, user)
            return redirect('home page')

        form = LoginForm(self.request.POST)
        for (_, field) in form.fields.items():
            field.widget.attrs['class'] = 'form-control'

        context = {
            'form': form
        }
        return render(self.request, 'accounts/sign_in.html', context=context)


def sign_out_view(req):
    logout(req)
    return redirect('home page')


def delete_profile_view(req, pk):
    User.objects.get(pk=pk).delete()
    return redirect('home page')

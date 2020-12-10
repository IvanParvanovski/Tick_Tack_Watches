from django.contrib.auth import logout, login, authenticate
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from accounts.forms.login import LoginForm
from accounts.forms.profile import ProfileForm

from django.contrib.auth.models import User
from django.views.generic import DetailView

from accounts.models import UserProfile


class Profile(DetailView):
    template_name = 'accounts/profile.html'
    model = User


class UserSignUp(CreateView):
    form_class = ProfileForm
    template_name = 'accounts/sign_up.html'
    success_url = reverse_lazy('display watches')

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

    def form_valid(self, form):
        user = authenticate(**form.cleaned_data)
        if user:
            login(self.request, user)
            return redirect('home page')

        context = {
            'form': LoginForm(self.request.POST)
        }
        return render(self.request, 'accounts/sign_in.html', context=context)


def sign_out_view(req):
    logout(req)
    return redirect('home page')

from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from accounts.forms.login import LoginForm


class UserSignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/sign_up.html'
    success_url = reverse_lazy('display watches')

    def form_valid(self, form):
        user = form.save()
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

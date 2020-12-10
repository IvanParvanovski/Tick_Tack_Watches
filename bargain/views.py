from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from accounts.models import UserProfile
from bargain.models import Purchase


@login_required
def create_purchase(req, user_pk, watch_pk):
    purchase = Purchase(user_id=user_pk, watch_id=watch_pk)
    purchase.save()
    return redirect('purchases', user_pk)


@login_required(login_url='/accounts/sign_in/')
def show_purchases(req, pk):
    profile = UserProfile.objects.get(pk=pk)
    context = {
        'profile': profile,
        'purchases': profile.purchase_set.all(),
    }

    return render(req, 'bargain/purchases.html', context=context)

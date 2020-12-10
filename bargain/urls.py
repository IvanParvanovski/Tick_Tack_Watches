from django.urls import path

from bargain.views import show_purchases, create_purchase

urlpatterns = (
    path('<int:pk>/', show_purchases, name='purchases'),
    path('add_purchase/<int:user_pk>/<int:watch_pk>', create_purchase, name='create purchase'),
)

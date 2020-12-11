from django.urls import path

from watches.views import WatchesListView, WatchDetailView, delete_watch, WatchUpdateView, WatchCreateView

urlpatterns = (
    path('<str:gender>', WatchesListView.as_view(), name='display watches'),
    path('details/<int:pk>', WatchDetailView.as_view(), name='watch details'),
    path('create_watch/', WatchCreateView.as_view(), name='create watch'),
    path('edit_watch/<int:pk>', WatchUpdateView.as_view(), name='edit watch'),
    path('delete_watch/<int:pk>', delete_watch, name='delete watch'),
)

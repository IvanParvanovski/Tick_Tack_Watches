from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from watches.models.watch import Watch


class WatchesListView(ListView):
    model = Watch
    context_object_name = 'watches'
    template_name = 'watches/watches_display.html'


class WatchDetailView(DetailView):
    model = Watch
    context_object_name = 'watch'
    template_name = 'watches/watch_details.html'


class WatchCreateView(CreateView):
    fields = '__all__'
    model = Watch
    template_name = 'watches/watch_create.html'
    success_url = reverse_lazy('display watches')


class WatchUpdateView(UpdateView):
    fields = '__all__'
    model = Watch
    context_object_name = 'watch'
    template_name = 'watches/watch_update.html'
    success_url = reverse_lazy('display watches')


def delete_watch(req, pk):
    Watch(pk=pk).delete()
    return redirect('display watches')

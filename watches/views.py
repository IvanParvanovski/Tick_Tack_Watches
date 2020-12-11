from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from watches.models.watch import Watch


class WatchesListView(ListView):
    model = Watch
    template_name = 'watches/watches_display.html'
    context_object_name = 'watches'
    paginate_by = 2

    def get_queryset(self):
        gender = self.kwargs['gender']
        if gender == 'all':
            return Watch.objects.all()
        return Watch.objects.filter(gender=gender)


class WatchDetailView(DetailView):
    model = Watch
    context_object_name = 'watch'
    template_name = 'watches/watch_details.html'


class WatchCreateView(CreateView):
    fields = '__all__'
    model = Watch
    template_name = 'watches/watch_create.html'
    success_url = reverse_lazy('display watches', kwargs={'gender': 'all'})


class WatchUpdateView(UpdateView):
    fields = '__all__'
    model = Watch
    context_object_name = 'watch'
    template_name = 'watches/watch_update.html'
    success_url = reverse_lazy('display watches', kwargs={'gender': 'all'})


def delete_watch(req, pk):
    Watch(pk=pk).delete()
    return redirect('display watches', 'all')

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from watches.models.watch import Watch
from watches.models.watch_description import WatchDescription


class WatchesListView(ListView):
    model = Watch
    template_name = 'watches/watches_display.html'
    context_object_name = 'watches'
    paginate_by = 6

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

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for (_, field) in form.fields.items():
            field.widget.attrs['class'] = 'form-control'
        return form


class WatchUpdateView(UpdateView):
    fields = '__all__'
    model = Watch
    context_object_name = 'watch'
    template_name = 'watches/watch_update.html'
    success_url = reverse_lazy('display watches', kwargs={'gender': 'all'})

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for (_, field) in form.fields.items():
            field.widget.attrs['class'] = 'form-control'
        return form


class WatchCreateDescription(CreateView):
    model = WatchDescription
    fields = ('dial_colour',
              'strap_colour',
              'chronograph',
              'water_resistance',
              'case_shape',
              'analogue_or_digital')

    template_name = 'watches/watch_description_add.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for (_, field) in form.fields.items():
            field.widget.attrs['class'] = 'form-control'
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['watch_id'] = self.kwargs['pk']
        return context

    def form_valid(self, form):
        watch_id = self.kwargs['pk']
        description = form.save(commit=False)
        description.watch = Watch.objects.get(pk=watch_id)
        description.save()
        return redirect('watch details', watch_id)


class WatchUpdateDescription(UpdateView):
    model = WatchDescription
    template_name = 'watches/watch_description_update.html'
    fields = ('dial_colour',
              'strap_colour',
              'chronograph',
              'water_resistance',
              'case_shape',
              'analogue_or_digital')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for (_, field) in form.fields.items():
            field.widget.attrs['class'] = 'form-control'
        return form

    def get_success_url(self):
        return reverse_lazy('watch details', kwargs={'pk': self.object.watch.id})


def delete_watch(req, pk):
    Watch(pk=pk).delete()
    return redirect('display watches', 'all')

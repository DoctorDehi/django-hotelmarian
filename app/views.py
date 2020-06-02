from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.core.exceptions import ObjectDoesNotExist

from .models import *
from .forms import RezervaceForm

# Create your views here.
class IndexView(ListView):
    template_name = 'app/index.html'
    model = Pokoj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pokoje = []
        for pokoj in context['object_list']:
            try:
                obrazek = ObrazekPokoje.objects.get(pokoj=pokoj.id).obrazek_url
            except ObjectDoesNotExist as e:
                obrazek = 'app/img/pokoje/default.png'

            pokoje.append({
                'objekt' : pokoj,
                'obrazek' : obrazek,
            })
        context['pokoje'] = pokoje
        return context

class DetailPokojeView(DetailView):
    template_name = 'app/detailpokoje.html'
    model = Pokoj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            obrazek = ObrazekPokoje.objects.get(pokoj=context['object'].id).obrazek_url
        except ObjectDoesNotExist as e:
            obrazek = 'app/img/pokoje/default.png'
        context["obrazek"] = obrazek
        return context

class RezervovatPokojView(FormView):
    template_name = 'app/rezervace.html'
    form_class = RezervaceForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        context = self.get_context_data()
        context['message'] = {'text':'Rezervace byla úspěšně přijata.',
                              'class' : 'text-success'
                              }
        return self.render_to_response(context)



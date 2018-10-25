from django.shortcuts import render
from django.views.generic import ListView

from . import models as base_mod


def home(request):
    return render()


class HomePage(ListView):
    model = base_mod.Image
    template_name = 'home.html'

    def get_queryset(self):
        pass

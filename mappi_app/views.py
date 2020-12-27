from django.views.generic import ListView, DetailView
from .models import Store


class StoreList(ListView):
    template_name = 'mappi_app/list.html'
    model = Store

class StoreDetail(DetailView):
    template_name = 'mappi_app/detail.html'
    model = Store
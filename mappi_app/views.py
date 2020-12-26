from django.views.generic import ListView
from .models import Store


class StoreList(ListView):
    template_name = 'list.html'
    model = Store
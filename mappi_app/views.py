from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect
from .models import Store, Review


class StoreList(ListView):
    template_name = "mappi_app/list.html"
    model = Store


class StoreDetail(DetailView):
    template_name = "mappi_app/detail.html"
    model = Store


class StoreCreate(CreateView):
    template_name = "mappi_app/create.html"
    model = Store
    fields = ("store_name", "store_adress", "store_link", "store_image")
    success_url = reverse_lazy("list")


class StoreMap(TemplateView):
    template_name = "mappi_app/map.html"


class StoreReview(CreateView):
    template_name = "mappi_app/review.html"
    model = Review
    fields = ("store", "user", "review_sentence", "review_score")

    def get_initial(self):
        review_score = 3
        store = get_object_or_404(Store, id=self.kwargs.get("pk"))
        return {"review_score": review_score, "store": store}


class StoreMapDetail(DetailView):
    template_name = "mappi_app/map.html"
    model = Store


def update_went_flag(request):
    pk = request.POST.get("button")
    store = get_object_or_404(Store, id=pk)
    if store.went_flag:
        store.went_flag = False
    else:
        store.went_flag = True
    store.save()
    return redirect("mappi_app:store_map_detail", pk=pk)

from django.urls import path
from .views import (
    StoreList,
    StoreDetail,
    StoreCreate,
    StoreMap,
    StoreReview,
    StoreMapDetail,
    update_went_flag,
)

app_name = "mappi_app"

urlpatterns = [
    path("list/", StoreList.as_view(), name="list"),
    path("detail/<int:pk>", StoreDetail.as_view(), name="detail"),
    path("create/", StoreCreate.as_view(), name="create"),
    path("", StoreMap.as_view()),
    path("review/<int:pk>", StoreReview.as_view()),
    path("<int:pk>", StoreMapDetail.as_view(), name="store_map_detail"),
    path("update_went_flag/", update_went_flag, name="update_went_flag"),
]
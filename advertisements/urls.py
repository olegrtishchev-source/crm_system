from django.urls import path

from . import views

app_name = "advertisements"  # pylint: disable=invalid-name

urlpatterns = [
    path("", views.AdvertisementListView.as_view(), name="list"),
    path("new/", views.AdvertisementCreateView.as_view(), name="create"),
    path("<int:pk>/", views.AdvertisementDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.AdvertisementUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.AdvertisementDeleteView.as_view(), name="delete"),
]

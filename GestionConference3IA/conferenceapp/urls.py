from django.urls import path
from . import views
from .views import *

urlpatterns = [
 #path("list/", views.list_conferences, name="list_conferences"),
    path("list/", ConferenceList.as_view(), name="list_conferences"),
    path("<int:pk>/", ConferenceDetail.as_view(), name="conference_detail"),
    path("add/", ConferenceCreate.as_view(), name="conference_add"),
    path("edit/<int:pk>/", ConferenceUpdate.as_view(), name="conference_update"),
    path("delete/<int:pk>/", ConferenceDelete.as_view(), name="conference_delete"),
    path("index/", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]

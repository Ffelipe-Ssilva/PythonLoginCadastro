from django.urls import path

from . import views

app_name = "cadlogapp"

urlpatterns=[
    path("",views.HomePageView.as_view(), name="home"),
]
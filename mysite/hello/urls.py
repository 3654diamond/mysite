from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("mahesh", views.mahesh, name="mahesh"),
    path("mad", views.mad, name="mad"),
    path("<str:name>" , views.greet, name="index")
]
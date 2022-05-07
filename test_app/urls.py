from django.urls import path

from . import views


urlpatterns = [
    path("datetime/", views.DatetimeView.as_view()),
]

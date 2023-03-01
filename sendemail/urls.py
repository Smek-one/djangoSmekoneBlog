from django.contrib import admin
from django.urls import path

from .views import contactView, successView

urlpatterns = [
    path("sendmail/contact/", contactView, name="contact"),
    path("sendmail/success/", successView, name="success"),
]
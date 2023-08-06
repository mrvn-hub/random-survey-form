from django.urls import path
from . import views


urlpatterns = [
	path("", views.index, name="index"),
	path("submit", views.register_session, name="register_session")
]

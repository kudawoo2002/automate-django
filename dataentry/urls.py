from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("import_data/", views.import_data, name="import_data"),
    path("export_data/", views.export_data, name="export_data")
]
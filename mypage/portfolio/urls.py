from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path("", views.PortfolioView.as_view(), name="portfolio"),
    path("copy/", views.TestView.as_view(), name="copy"),
]

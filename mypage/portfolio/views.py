from django.shortcuts import render
from django.views import generic

# Create your views here.


class PortfolioView(generic.TemplateView):
    template_name = "portfolio/index.html"


class TestView(generic.TemplateView):
    template_name = "portfolio/copy.html"

from django.shortcuts import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"

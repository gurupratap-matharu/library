from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'catalog/home.html'


class SearchResultsView(TemplateView):
    template_name = 'catalog/search_results.html'

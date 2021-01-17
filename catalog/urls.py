from django.urls import path

from catalog.views import HomePageView, SearchResultsView

app_name = 'catalog'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('search/', SearchResultsView.as_view(), name='search'),
]

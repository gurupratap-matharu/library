from django.urls import path

from catalog.views import HomePageView

app_name = 'catalog'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]

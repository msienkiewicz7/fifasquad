from django.urls import path
from .views import search, SquadBuilderView
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('search/', search, name="search_results"),
    path('squadbuilder/', TemplateView.as_view(template_name='squad_builder.html'), name='squadbuilder'),
    path('squadbuilder/build/', SquadBuilderView.as_view(), name='build'),
]

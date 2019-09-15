from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from unidecode import unidecode

from .models import Player


# Create your views here.

def search(request):
    query = request.GET.get('q')
    search_result = Player.objects.filter(
        Q(name__icontains = query) |
        # Q(nationality__iexact = query) |
        Q(nationality__icontains = query) |
        Q(club__icontains = query)

    ).distinct()

    paginator = Paginator(search_result, 10)

    page = request.GET.get('page')
    players = paginator.get_page(page)
    return render(request, 'search_results.html', {'players': players, 'query': query})

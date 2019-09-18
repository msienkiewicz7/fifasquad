from django.shortcuts import render
from django.views import View
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Player

import logging
logger = logging.getLogger('django')

# Create your views here.

def search(request):
    query = request.GET.get('q')
    search_result = Player.objects.filter(
        Q(name__icontains = query) |
        Q(nationality__icontains = query) |
        Q(club__icontains = query)

    ).distinct()

    paginator = Paginator(search_result, 10)

    page = request.GET.get('page')
    players = paginator.get_page(page)
    # logger.info(query)
    return render(request, 'search_results.html', {'players': players, 'query': query})



class SquadBuilderView(View):
    formations = {
        '433': ['GK', 'LB', 'CB', 'CB', 'RB', 'LM', 'CM', 'RM', 'LF', 'ST', 'RF'],
        '442': ['GK', 'LB', 'CB', 'CB', 'RB', 'LM', 'CM', 'CM', 'RM', 'LF', 'RF'],
        '352': ['GK', 'CB', 'CB', 'CB', 'LM', 'CDM', 'CAM', 'CDM', 'RM', 'LF', 'RF'],
        '451': ['GK', 'LB', 'CB', 'CB', 'RB', 'LM', 'CDM', 'CAM', 'CDM', 'RM', 'ST']
    }


    def get(self, request):
        budget = budget_left = float(request.GET.get('b')) * 1000000
        team = []

        formation = request.GET.get('p')
        positions = self.formations[formation]

        for pos in positions:
            players_left = 11-len(team)
            players = Player.objects.filter(
                Q(value__lte = budget_left/players_left),
                Q(position__exact = pos),
                ~Q(value__exact = 0) # Ignore free players
            )
            # Select first player from list orderd by overall
            player = players[0]
            # Disable duplicates in case of repeting positions
            if player in team:
                player = players[1]

            budget_left -= float(player.value)
            team.append(player)

        # format budget, add thousend seperator (e.g: 1000000 to 1.000.000)
        budget_str = "{:,}".format(budget).replace(',', '.')
        # format float without trailing zeros
        budget = '{0:g}'.format(budget / 1000000)

        return render(request, 'team.html', {'budget': budget, 'budget_left': budget_left, 'team': team})

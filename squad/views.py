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

    # get team value in milions
    def get_team_value(self, team):
        value = 0
        for player in team:
            value += player.value
        return value/1000000

    def get_team_overall(self, team):
        overall = 0
        for player in team:
            overall += player.overall
        return int(overall/len(team))

    # Disable duplicates in case of repeting positions
    def get_first_new_player(self, players, team):
        if not players[0] in team:
            return players[0]
        elif not players[1] in team:
            return players[1]
        elif not players[2] in team:
            return players[2]

        # for player in players:
        #     if not player in team:
        #         return player


    def get(self, request):
        try:
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
                player = self.get_first_new_player(players, team)

                budget_left -= float(player.value)
                team.append(player)


        # if no players found (line 58) break the squad-builder loop
        except IndexError:
            team = None

        # if wrong formation in query set defaulf foramtion
        except KeyError:
            formation = self.formations['433']


        budget = '{0:g}'.format(budget / 1000000)


        return render(request, 'team.html', {'budget': budget, 'team': team, 'team_value': self.get_team_value(team), 'team_overall': self.get_team_overall(team)})

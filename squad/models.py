from django.db import models
from django.db.models import Q

# Create your models here.

class PlayerSet(models.QuerySet):
    # find the best player for specific price at spec. position that is not already in team
    def best_player(self, player_budget, position, team):
        players_to_exclude = [o.name for o in team]
        return Player.objects.filter(
            Q(value__lte = player_budget),
            Q(position__exact = position),
            ~Q(value__exact = 0) # ignore free players
        ).exclude(
            name__in = players_to_exclude
        ).order_by('-overall', 'age', '-value'
        ).first()


class Player(models.Model):
    row = models.IntegerField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    age = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    photo = models.CharField(max_length=100, blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True, null=True)
    flag = models.CharField(max_length=100, blank=True, null=True)
    overall = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    potential = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    club = models.CharField(max_length=100, blank=True, null=True)
    club_logo = models.CharField(max_length=100, blank=True, null=True)
    value = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    # value = models.CharField(max_length=100, blank=True, null=True)
    wage = models.CharField(max_length=100, blank=True, null=True)
    special = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

    preferred_foot = models.CharField(max_length=100, blank=True, null=True)
    international_reputation = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    weak_foot = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    skill_moves = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    work_rate = models.CharField(max_length=100, blank=True, null=True)
    body_type = models.CharField(max_length=100, blank=True, null=True)
    real_face = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    jersey_number = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    joined = models.CharField(max_length=100, blank=True, null=True)
    loaned_from = models.CharField(max_length=100, blank=True, null=True)
    contract_valid_until = models.CharField(max_length=100, blank=True, null=True)
    height = models.CharField(max_length=100, blank=True, null=True)
    weight = models.CharField(max_length=100, blank=True, null=True)

    ls = models.CharField(max_length=100, blank=True, null=True)
    st = models.CharField(max_length=100, blank=True, null=True)
    rs = models.CharField(max_length=100, blank=True, null=True)
    lw = models.CharField(max_length=100, blank=True, null=True)
    lf = models.CharField(max_length=100, blank=True, null=True)
    cf = models.CharField(max_length=100, blank=True, null=True)
    rf = models.CharField(max_length=100, blank=True, null=True)
    rw = models.CharField(max_length=100, blank=True, null=True)
    lam = models.CharField(max_length=100, blank=True, null=True)
    cam = models.CharField(max_length=100, blank=True, null=True)
    ram = models.CharField(max_length=100, blank=True, null=True)
    lm = models.CharField(max_length=100, blank=True, null=True)
    lcm = models.CharField(max_length=100, blank=True, null=True)
    cm = models.CharField(max_length=100, blank=True, null=True)

    rcm = models.CharField(max_length=100, blank=True, null=True)
    rm = models.CharField(max_length=100, blank=True, null=True)
    lwb = models.CharField(max_length=100, blank=True, null=True)
    ldm = models.CharField(max_length=100, blank=True, null=True)
    cdm = models.CharField(max_length=100, blank=True, null=True)
    rdm = models.CharField(max_length=100, blank=True, null=True)
    rwb = models.CharField(max_length=100, blank=True, null=True)
    lb = models.CharField(max_length=100, blank=True, null=True)
    lcb = models.CharField(max_length=100, blank=True, null=True)
    cb = models.CharField(max_length=100, blank=True, null=True)
    rcb = models.CharField(max_length=100, blank=True, null=True)
    rb = models.CharField(max_length=100, blank=True, null=True)

    crossing = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    finishing = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    headingaccuracy = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    shortpassing = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    volleys = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    dribbling = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    curve = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)

    fkaccuracy = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    longpassing = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    ballcontrol = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    acceleration = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    sprintspeed = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    agility = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    reactions = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    balance = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    shotpower = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    jumping = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    stamina = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    strength = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    longshots = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    aggression = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    interceptions = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    positioning = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    vision = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    penalties = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    composure = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    marking = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    standingtackle = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    slidingtackle = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    gkdiving = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    gkhandling = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    gkkicking = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    gkpositioning = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    gkreflexes = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    release_clause = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'players'
        # ordering = ['-overall', 'age', '-value']

    objects = PlayerSet.as_manager()

    def __str__(self):
        return "%s %s" % (self.name, self.position)

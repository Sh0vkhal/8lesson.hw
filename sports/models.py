from django.db import models



class Team(models.Model):
    name = models.CharField(max_length=100)
    sport = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    roster = models.ManyToManyField('Player', related_name='teams')
    coaching_staff = models.TextField()

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    skills = models.TextField()  
   

    def __str__(self):
        return self.name


class Game(models.Model):
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_games')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_games')
    score_team1 = models.IntegerField(default=0)
    score_team2 = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.team1} vs {self.team2} on {self.date}"


class Season(models.Model):
    name = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    participating_teams = models.ManyToManyField(Team)
    schedule = models.ManyToManyField(Game, blank=True)
    results = models.TextField()

    def __str__(self):
        return f"{self.name} {self.year}"

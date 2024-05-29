from django.db import models

class MoviesData(models.Model):
    year = models.CharField(max_length=50, default = '0')
    title = models.CharField(max_length=255)
    nominations = models.CharField(max_length=50)
    awards = models.CharField(max_length=50)
    
    def __str__(self):
        return (f"Year : {self.year}, Title : {self.title}, Nominations : {self.nominations}, Awards : {self.awards}")


class HockeyTeamsData(models.Model):
    team_name = models.CharField(max_length=255)
    year = models.CharField(max_length=50)
    wins = models.CharField(max_length=50,default = '0')
    losses = models.CharField(max_length=50)
    win_percent = models.CharField(max_length=50)
    goals_for =  models.CharField(max_length=50)
    goals_against = models.CharField(max_length=50)
    plus_minus = models.CharField(max_length=50)

    def __str__(self):
        return (f"{self.team_name} - Year: {self.year}, Wins: {self.wins}, Losses: {self.losses}, "
                f"Win%: {self.win_percent}, Goals For: {self.goals_for}, Goals Against: {self.goals_against}, "
                f"Plus/Minus: {self.plus_minus}")
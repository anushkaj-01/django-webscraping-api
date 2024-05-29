from rest_framework import serializers
from .models import *

class MoviesDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviesData
        fields = ['year' ,'title', 'nominations', 'awards']

class HockeyTeamsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HockeyTeamsData
        fields = ['team_name', 'year', 'wins', 'losses', 'win_percent', 'goals_for', 'goals_against', 'plus_minus']

from django.contrib import admin
from .models import MoviesData, HockeyTeamsData

admin.site.register(MoviesData)
class MoviesDataAdmin(admin.ModelAdmin):
    list_display = ('year','title', 'nominations', 'awards')
    search_fields = ('title', 'nominations', 'awards')

admin.site.register(HockeyTeamsData)
class HockeyTeamsDataAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'year', 'wins', 'losses', 'win_percent', 'goals_for', 'goals_against', 'plus_minus')
    search_fields = ('team_name', 'year')


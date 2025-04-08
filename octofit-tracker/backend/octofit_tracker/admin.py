from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout

# Removed registration of plain Python classes as they are not compatible with Django admin
# admin.site.register(User)
# admin.site.register(Team)
# admin.site.register(Activity)
# admin.site.register(Leaderboard)
# admin.site.register(Workout)

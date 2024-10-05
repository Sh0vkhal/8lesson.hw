from django.contrib import admin

# Register your models here.
from .models import Team,Player,Game,Season

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Game)
admin.site.register(Season)

from django.contrib import admin
from characters.models import Character, Rankings


class charactersAdmin(admin.ModelAdmin):
    related_lookup_fields = { 'characterName': ['characterName']}
    list_display = ('portrait','characterName','server','level','itemLevelEquipped','itemLevel','lastArmoryUpdate','lastWLUpdate','description')
admin.site.register(Character, charactersAdmin)

class rankingsAdmin(admin.ModelAdmin):
    related_lookup_fields = { 'id': ['id']}
    list_display = ('id','characterID','encounterID','rankNumber','rankOutOf','difficulty','itemLevel')
admin.site.register(Rankings, rankingsAdmin)
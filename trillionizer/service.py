
from __future__ import unicode_literals
from django.http import HttpResponse
import datetime
#from characters.models import character
import urllib2
import json

def getCharacterInfo(id,serverName, characterName):
    url = str("https://us.api.battle.net/wow/character/") + str(serverName)+ str("/") + str(characterName) +  str("?locale=en_US&apikey=g5n7m2d499n6wumem7g6qqwkyzwfq8pn")
    response = urllib2.urlopen(url)
    data = json.load(response)
    characterLevel = str(data['level'])
    faction = str(data['faction'])
    totalHonorableKills = str(data['totalHonorableKills'])
    icon = str("https://render-api-us.worldofwarcraft.com/static-render/us/") + str(data['thumbnail'])
    race = str(data['race'])
    achivementPoints = str(data['achievementPoints'])
    gender = str(data['gender'])
    gameClass = str(data['class'])
    return icon



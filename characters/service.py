
from __future__ import unicode_literals
from django.http import HttpResponse
import datetime
from characters.models import Character
from characters.models import Rankings
import urllib2
import json

def getCharacterInfo(serverName, characterName):
    url = str("https://us.api.battle.net/wow/character/") + str(serverName)+ str("/") + str(characterName) +  str("?locale=en_US&fields=items&apikey=g5n7m2d499n6wumem7g6qqwkyzwfq8pn")
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
    itemLevel = str(data['items']['averageItemLevel'])
    itemLevelEquipped = str(data['items']['averageItemLevelEquipped'])
    if Character.objects.filter(characterName=characterName,server=serverName).count() > 0:
        updatedCharacter =  Character.objects.get(characterName=characterName,server=serverName)
        updatedCharacter.itemLevel = itemLevel
        updatedCharacter.race = race
        updatedCharacter.gender = gender
        updatedCharacter.gameClass = gameClass
        updatedCharacter.itemLevelEquipped = itemLevelEquipped
        updatedCharacter.lastArmoryUpdate = datetime.datetime.now()
        updatedCharacter.iconURL = icon
        updatedCharacter.level = characterLevel
        updatedCharacter.characterHonorableKills = totalHonorableKills
        updatedCharacter.faction = faction
        updatedCharacter.achivementPoints = achivementPoints
        updatedCharacter.save()
        return 'Updated Character'
    else:
        newCharacter = Character(characterName=characterName,server=serverName,level=characterLevel,itemLevel=itemLevel,itemLevelEquipped=itemLevelEquipped,lastArmoryUpdate=datetime.datetime.now(),characterHonorableKills=totalHonorableKills,achivementPoints=achivementPoints,gender=gender,race=race,iconURL=icon)
        newCharacter.save()
        return 'Created Character'

def getCharacterRankings(serverName, characterName):
    url = str("https://www.warcraftlogs.com:443/v1/rankings/character/") + str(characterName) + str('/') + str(serverName) + str("/US?api_key=958f158abe76b3d94e5e16fecbdce32e")
    response = urllib2.urlopen(url)
    data = json.load(response)
    for ranking in data:
        reportID = str(ranking['reportID'])
        total = str(ranking['total'])
        encounterID = str(ranking['encounter'])
        if Rankings.objects.filter(reportID=reportID,encounterID=encounterID,total=total).count() > 0:
            print 'Already Imported'
        else:
            guildName = str(ranking['guild'])
            encounterID = str(ranking['encounter'])
            spec = str(ranking['spec'])
            guildName = str(ranking['guild'])
            rankNumber = str(ranking['rank'])
            rankOutOf = str(ranking['outOf'])
            duration = str(ranking['duration'])
            reportID = str(ranking['reportID'])
            fightID = str(ranking['fightID'])
            difficulty = str(ranking['difficulty'])
            size = str(ranking['size'])
            itemLevel = str(ranking['itemLevel'])
            total = str(ranking['total'])
            characterID = Character.objects.get(characterName=characterName).id
            newRanking = Rankings(characterID_id=characterID,encounterID=encounterID,spec=spec,guildName=guildName,rankNumber=rankNumber,rankOutOf=rankOutOf,duration=duration,reportID=reportID,fightID=fightID,difficulty=difficulty,size=size,itemLevel=itemLevel,total=total)
            newRanking.save()
    return 'Finished'






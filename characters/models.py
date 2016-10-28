from django.db import models
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Character(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    characterName = models.CharField(db_column='characterName', verbose_name='Character Name:', max_length=255, blank=True, null=True)  # Field name made lowercase.
    server = models.CharField(db_column='serverName',max_length=255, blank=True, null=True)
    level = models.IntegerField(db_column='characterLevel', blank=True, null=True)  # Field name made lowercase.
    itemLevel = models.IntegerField(db_column='itemLevel', blank=True, null=True)  # Field name made lowercase.
    itemLevelEquipped = models.IntegerField(db_column='itemLevelEquipped',verbose_name='Equipped', blank=True, null=True)  # Field name made lowercase.
    lastArmoryUpdate = models.DateTimeField(db_column='lastArmoryUpdate', max_length=255, blank=True, null=True)
    lastWLUpdate = models.DateTimeField(db_column='lastWLUpdate', verbose_name='Last Warcraft Logs Update', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='description', verbose_name='Character Description', max_length=255, blank=True, null=True)
    characterHonorableKills = models.IntegerField(db_column='characterHonorableKills', verbose_name='Character Honorable Kills', blank=True, null=True)
    achivementPoints = models.IntegerField(db_column='achievementPoints', verbose_name='Achievement Points', blank=True, null=True)
    gender = models.CharField(db_column='gender', verbose_name='Gender', max_length=255, blank=True, null=True)
    race = models.CharField(db_column='race', verbose_name='Race', max_length=255, blank=True, null=True)
    iconURL = models.CharField(db_column='iconURL', verbose_name='Icon URLS', max_length=1000, blank=True, null=True)
    nickName = models.CharField(db_column='nickName', verbose_name='Nickname', max_length=255, blank=True, null=True)
    def portrait(self):
        return str('<img style="width:50px;height:50px;border-radius: 10px;" src="') + str(self.iconURL) + str('"/>')
    portrait.allow_tags = True

    def __str__(self):
        return self.characterName


class Rankings(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    characterID = models.ForeignKey(Character,db_column='characterID', verbose_name='Character', blank=True, null=True)  # Field name made lowercase.
    encounterID = models.IntegerField(db_column='encounterID', blank=True, null=True)
    spec = models.IntegerField(db_column='spec', blank=True, null=True)  # Field name made lowercase.
    guildName = models.CharField(db_column='guildName', blank=True, max_length=255, null=True)  # Field name made lowercase.
    rankNumber = models.IntegerField(db_column='rankNumber',verbose_name='Rank Number', blank=True, null=True)  # Field name made lowercase.
    rankOutOf = models.IntegerField(db_column='rankOutOf', blank=True, null=True)
    duration = models.IntegerField(db_column='duration', verbose_name='Duration', blank=True, null=True)  # Field name made lowercase.
    reportID = models.CharField(db_column='reportID', max_length=255, verbose_name='Report ID', blank=True, null=True)
    fightID = models.IntegerField(db_column='fightID', verbose_name='Fight ID', blank=True, null=True)
    difficulty = models.IntegerField(db_column='difficulty', verbose_name='Difficulty', blank=True, null=True)
    size = models.IntegerField(db_column='raidSize', verbose_name='Raid Sie',  blank=True, null=True)
    itemLevel = models.IntegerField(db_column='itemLevel', verbose_name='Item Level', blank=True, null=True)
    total = models.FloatField(db_column='total', verbose_name='total', blank=True, null=True)
   
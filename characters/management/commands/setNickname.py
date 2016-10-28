from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('character', nargs='+', type=str)
        parser.add_argument('nickName', nargs='+', type=str)
    def handle(self, *args, **options):
        from characters.models import Character
        characterName = ''
        nickName = ''
        for character in options['character']:
            characterName = character
        for nick in options['nickName']:
            nickName = nick
        thecharacter = Character.objects.get(characterName=characterName, server='Area-52')
        thecharacter.nickName = nickName
        thecharacter.save()
        print thecharacter.nickName + str(' has been updated.')

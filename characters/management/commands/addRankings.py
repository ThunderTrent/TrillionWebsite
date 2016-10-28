from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('character', nargs='+', type=str)
        parser.add_argument('serverName', nargs='+', type=str)
    def handle(self, *args, **options):
        from characters.service import getCharacterRankings
        characterName = ''
        serverName = ''
        for character in options['character']:
            characterName = character
        for server in options['serverName']:
            serverName = server
        results = getCharacterRankings(serverName,characterName)

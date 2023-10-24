from django.core.management import BaseCommand

from habits.models import Location


class Command(BaseCommand):

    def handle(self, *args, **options):
        Location.objects.create(
            location="любое место"
        )

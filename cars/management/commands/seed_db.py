from django.core.management.base import BaseCommand
from cars.models import Brand  # Import your models here

class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        # Example seeding logic
        if Brand.objects.exists():
            self.stdout.write(self.style.WARNING('Database already seeded'))
            return

        Brand.objects.create(
            name='SUZUKI',
        )

        self.stdout.write(self.style.SUCCESS('Database seeded successfully'))

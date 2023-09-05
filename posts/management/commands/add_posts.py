import csv

from django.core.management.base import BaseCommand
from django.conf import settings

from posts.models import Author,Post,Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Deleting existing data........")

        Category.objects.all().delete()
        Post.objects.all().delete()
        Author.objects.all().delete()

        file = open(settings.BASE_DIR / "new_posts.csv")
        csv_reader = csv.reader(file)

        next(csv_reader)

        for row in csv_reader:
            author_name = row[1].split(",")[0]
            content = row[2]
            date = row[3]
            tags = row[5]
            title = row[6]

            print(title)
        
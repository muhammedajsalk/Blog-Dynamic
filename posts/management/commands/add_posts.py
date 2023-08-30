from django.core.management.base import BaseCommand
from posts.models import Author,Post,Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Deleting existing data........")

        Category.objects.all().delete()
        Post.objects.all().delete()
        Author.objects.all().delete()
        
        
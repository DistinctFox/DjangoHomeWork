import csv
from django.utils.text import slugify
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    help = 'importing csv file into DB'

    def add_arguments(self, parser):
        parser.add_argument(
            'path',
            type=str,
            help='path to csv file'
        )

    def handle(self, *args, **options):
        with open(options['path'], 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            phone_model = Phone(
                id=phone['id'],
                name=phone['name'],
                image=phone['image'],
                price=phone['price'],
                release_date=phone['release_date'],
                lte_exists=phone['lte_exists'],
                slug=slugify(phone['name']))

            phone_model.save()

from django.core.management.base import BaseCommand, CommandError
from dataentry.models import Student
from django.apps import apps
import csv


class Command(BaseCommand):
    help = "Insert data from csv to the database"

    def add_arguments(self, parser):
        parser.add_argument('file_path',type=str, help="specifies file path")
        parser.add_argument('model_name',type=str, help="name of the model")

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        model_name = kwargs['model_name'].capitalize()

        # Search for model accross all install apps
        model = None
        for app_config in apps.get_app_configs():
            # Try to search the model
            try:
                model = apps.get_model(app_config.label, model_name) 
                break
            except LookupError:
                continue
        
        if not model:
            raise CommandError(f"model '{model_name}' not found in any apps")

        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                model.objects.create(**row)
                # roll_no = row['roll_no']
                # exist_rows = model.objects.filter(roll_no=roll_no).exists()
                # if not exist_rows:
                #     model.objects.create(**row)
                # else:
                #     self.stdout.write(self.style.WARNING(f"Student roll_no {roll_no} already exist"))

        self.stdout.write(self.style.SUCCESS("Data was imported from csv succesfully "))
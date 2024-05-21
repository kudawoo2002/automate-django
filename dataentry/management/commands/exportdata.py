from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
import csv
from dataentry.utils import generate_csv_file
import datetime


class Command(BaseCommand):
    help = "Export data from table"

    def add_arguments(self, parser):
        parser.add_argument("model_name", type=str, help="model name")

    def handle(self, *args, **kwargs):
        model_name = kwargs['model_name'].capitalize()

        model = None

        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                break
            except LookupError:
                pass
        
        if not model:
            raise CommandError(f"model '{model_name}' not found in any apps")
            return

        # Get data from studens table
        data = model.objects.all()

        # filepath of the csv file
        file_path = generate_csv_file(model_name)
        
        # Write data to the csv file
        with open(file_path, 'w', newline="") as file:
            writer = csv.writer(file)

            # Write file header

            writer.writerow([field.name for field in model._meta.fields])

            # Write the data

            for dt in data:
                writer.writerow([getattr(dt, field.name) for field in model._meta.fields])

        
        self.stdout.write(self.style.SUCCESS("Data exported successfully"))


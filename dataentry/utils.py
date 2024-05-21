from django.apps import apps
from django.core.management.base import CommandError
from django.db import DataError
from django.core.mail import EmailMessage
from django.conf import settings
import csv


def get_all_custom_models():
    default_models = ['LogEntry', 'Permission','Group','ContentType', 'Session', 'User', 'Upload']
    models = []
    for model in apps.get_models():
        if model.__name__ not in default_models:
            models.append(model.__name__)
    return models


def check_csv_errors(file_path, model_name):
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
        
        # Get the model field name

        field_name = [field.name for field in model._meta.fields if field.name != 'id']
        
        try:
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                csv_header = reader.fieldnames

                # Compare model field name to csv header
                if field_name != csv_header:
                    raise  DataError(f"csv file doesn't much {model_name} table fields")
                
                    # roll_no = row['roll_no']
                    # exist_rows = model.objects.filter(roll_no=roll_no).exists()
                    # if not exist_rows:
                    #     model.objects.create(**row)
                    # else:
                    #     self.stdout.write(self.style.WARNING(f"Student roll_no {roll_no} already exist"))
        except Exception as e:
            raise e
        
        return model



def send_email_notification(mail_subject, message, to_email):
    try:
        from_email = settings.DEFAULT_FROM_EMAIL
        mail = EmailMessage(mail_subject,message,from_email, to=[to_email])
        mail.send()
    except Exception as e:
        raise e


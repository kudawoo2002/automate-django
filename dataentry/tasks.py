from awd_main.celery import app
from django.core.management import call_command
from django.core.mail import EmailMessage
from .utils import send_email_notification
from django.conf import settings





@app.task
def import_data_task(file_path, model_name):
     try:
         call_command("importcsvdata", file_path, model_name)
         
           
     except Exception as e:
          raise  e
     mail_subject = "Data imported"
     message = "Your csv data was succefully imported"
     to_email = settings.DEFAULT_TO_EMAIL
     send_email_notification(mail_subject, message, to_email)
     return "Data imported successfully"
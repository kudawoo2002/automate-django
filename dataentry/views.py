from django.shortcuts import render, redirect
from .utils import get_all_custom_models
from uploads.models import Upload
from django.core.management import call_command
from django.conf import settings
from django.contrib import messages
from dataentry.utils import check_csv_errors
from .tasks import import_data_task, export_data_task
# Create your views here.

def home(request):
    return render(request, "home.html")


def import_data(request):
    models = None
    if request.method == "POST":
       
        file_path = request.FILES.get("file_path")
        model_name = request.POST.get("model_name")
        

        # Store ebove details to Upload table
        upload_data =  Upload.objects.create(file=file_path, model_name=model_name)
        upload_data.save()

        # Full path
        relative_path = str(upload_data.file.url)
        base_path = str(settings.BASE_DIR)

        file_path = base_path + relative_path

        # Check for csv error
        try:
            check_csv_errors(file_path, model_name)
        except Exception as e:
            messages.error(request, str(e))
            return redirect('import_data')

        # Handle the import task
        import_data_task.delay(file_path, model_name)
        # Trigger commad for upload data

        messages.success(request, "Your data has been imported, you will be notify when is done")
       
        return redirect('import_data')
    
    else:
        models = get_all_custom_models()
    
    context = {
        'models': models,
    }
        
    return render(request, "dataentry/importdata.html", context=context)


def export_data(request):
    if request.method == "POST":
        model_name = request.POST.get("model_name")
        try:
            export_data_task.delay(model_name)
        except Exception as e:
            raise e

        messages.success(request, "Your data has been exported, you will be notify when is done")
        return redirect("export_data")
    else:
        models = get_all_custom_models()
        context = {
            'models': models,
        }
    return render(request, "dataentry/exportdata.html", context)
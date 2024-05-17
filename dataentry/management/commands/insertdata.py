from django.core.management.base import BaseCommand
from dataentry.models import Student


class Command(BaseCommand):
    help="It will insert data into your database"

    def handle(self, *args, **kwargs):
        # The logic of the command goes here
        # insert 1 data
        # Student.objects.create(roll_no=1000, name="Sitou", age=43)
        # Insert multiple data

        data = [
             {
            'roll_no':"1004","name":"Kofi","age":23
        },
        {
            'roll_no':"1002","name":"Adel","age":24
        },
        {
            'roll_no':"1003","name":"Zain","age":20
        },
        {
            'roll_no':"1005","name":"Jessy","age":10
        },
        {
            'roll_no':"1003","name":"Zain","age":20
        }
           ]


        for entry in data:
            roll_no =  entry['roll_no']
            exist_records = Student.objects.filter(roll_no=roll_no).exists()
            if not exist_records:
                Student.objects.create(roll_no=entry['roll_no'], name=entry['name'], age=entry['age'])
            else:
                self.stdout.write(self.style.WARNING(f"student roll_no {roll_no} already exist"))
            
        self.stdout.write(self.style.SUCCESS("Data was successfully insert into the database"))
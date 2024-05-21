# Generated by Django 5.0.6 on 2024-05-18 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0002_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=20)),
                ('employee_name', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=20)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=19)),
                ('retirement', models.DecimalField(decimal_places=2, max_digits=19)),
                ('other_benefits', models.DecimalField(decimal_places=2, max_digits=19)),
                ('total_benefits', models.DecimalField(decimal_places=2, max_digits=19)),
                ('total_compensation', models.DecimalField(decimal_places=2, max_digits=19)),
            ],
        ),
    ]
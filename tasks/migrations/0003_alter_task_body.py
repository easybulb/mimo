# Generated by Django 4.2.16 on 2024-10-09 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_task_options_remove_task_completed_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='body',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
    ]
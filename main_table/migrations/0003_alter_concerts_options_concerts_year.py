# Generated by Django 4.2.11 on 2024-05-19 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_table', '0002_alter_concerts_week_day'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='concerts',
            options={'verbose_name': 'Concert', 'verbose_name_plural': 'Concerts'},
        ),
        migrations.AddField(
            model_name='concerts',
            name='year',
            field=models.IntegerField(default=1900, verbose_name='Year'),
        ),
    ]

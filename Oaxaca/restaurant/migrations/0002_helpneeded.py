# Generated by Django 4.1.7 on 2023-03-06 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HelpNeeded',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_id', models.IntegerField()),
                ('helped', models.BooleanField(default=False)),
            ],
        ),
    ]
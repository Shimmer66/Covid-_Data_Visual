# Generated by Django 3.2.4 on 2021-07-02 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_nowcity'),
    ]

    operations = [
        migrations.AddField(
            model_name='nowcity',
            name='city',
            field=models.CharField(blank=True, db_column='city', max_length=255),
        ),
    ]

# Generated by Django 3.2.4 on 2021-07-02 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_nowcity_city'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='alldaycity',
            new_name='alldayprovince',
        ),
        migrations.AlterModelTable(
            name='alldayprovince',
            table='alldayprovince',
        ),
    ]

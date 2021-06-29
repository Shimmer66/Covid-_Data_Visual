# Generated by Django 3.2.4 on 2021-06-29 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RatingsExplicit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(blank=True, db_column='userID', max_length=255, null=True)),
                ('isbn', models.CharField(blank=True, db_column='ISBN', max_length=255, null=True)),
                ('bookrating', models.CharField(blank=True, db_column='bookRating', max_length=255, null=True)),
            ],
            options={
                'db_table': 'RatingsExplicit',
            },
        ),
        migrations.CreateModel(
            name='RatingsImplicit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(blank=True, db_column='userID', max_length=255, null=True)),
                ('isbn', models.CharField(blank=True, db_column='ISBN', max_length=255, null=True)),
                ('bookrating', models.CharField(blank=True, db_column='bookRating', max_length=255, null=True)),
            ],
            options={
                'db_table': 'RatingsImplicit',
            },
        ),
    ]

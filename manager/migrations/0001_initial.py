# Generated by Django 4.1.4 on 2022-12-23 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poem', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('added_to_book', models.BooleanField(default=False)),
            ],
        ),
    ]
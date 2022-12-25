# Generated by Django 4.1.4 on 2022-12-24 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.FileField(upload_to='pdf')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

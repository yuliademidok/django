# Generated by Django 3.2.9 on 2022-03-13 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publication_app', '0011_auto_20211215_2101'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-id']},
        ),
    ]

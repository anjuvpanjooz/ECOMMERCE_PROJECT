# Generated by Django 4.2.2 on 2023-06-28 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoping_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
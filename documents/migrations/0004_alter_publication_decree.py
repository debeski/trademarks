# Generated by Django 5.1.4 on 2025-02-07 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_remove_publication_company_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='decree',
            field=models.CharField(max_length=10, verbose_name='رقم القرار'),
        ),
    ]

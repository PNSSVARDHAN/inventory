# Generated by Django 3.1.6 on 2025-01-04 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20250104_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentinstallation',
            name='company_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='purchasehistory',
            name='company_name',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Company',
        ),
    ]

# Generated by Django 3.1.6 on 2025-01-02 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20250102_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasehistory',
            name='company_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='purchasehistory',
            unique_together={('product', 'company_name')},
        ),
    ]

# Generated by Django 2.2 on 2020-02-13 16:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20200213_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tender',
            name='physical_submission_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Physical Submission Date'),
        ),
        migrations.AlterField(
            model_name='tender',
            name='tech_bid_opening_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Technical Bid Opening Bid'),
        ),
        migrations.AlterField(
            model_name='tender',
            name='tender_submission_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Tender Submission Date'),
        ),
    ]
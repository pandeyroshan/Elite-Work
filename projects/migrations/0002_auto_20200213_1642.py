# Generated by Django 2.2 on 2020-02-13 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tender',
            name='physical_submission_date',
            field=models.DateField(auto_now_add=True, verbose_name='Physical Submission Date'),
        ),
        migrations.AlterField(
            model_name='tender',
            name='tech_bid_opening_date',
            field=models.DateField(auto_now_add=True, verbose_name='Technical Bid Opening Bid'),
        ),
        migrations.AlterField(
            model_name='tender',
            name='tender_submission_date',
            field=models.DateField(auto_now_add=True, verbose_name='Tender Submission Date'),
        ),
    ]
# Generated by Django 3.1.10 on 2021-05-26 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("release", "0016_auto_20210519_2247"),
    ]

    operations = [
        migrations.AlterField(
            model_name="release",
            name="change_case_link",
            field=models.CharField(
                blank=True, max_length=1024, null=True, verbose_name="change case ID"
            ),
        ),
    ]
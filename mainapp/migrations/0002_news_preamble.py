# Generated by Django 4.1.1 on 2022-10-10 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="preamble",
            field=models.CharField(
                blank=True, max_length=1024, null=True, verbose_name="Preambula"
            ),
        ),
    ]

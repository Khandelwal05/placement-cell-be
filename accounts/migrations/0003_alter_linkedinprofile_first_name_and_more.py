# Generated by Django 5.0.6 on 2024-06-05 08:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_alter_linkedinprofile_first_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="linkedinprofile",
            name="first_name",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="linkedinprofile",
            name="last_name",
            field=models.CharField(blank=True, default="", max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="linkedinprofile",
            name="linkedin_profile_url",
            field=models.URLField(blank=True),
        ),
    ]
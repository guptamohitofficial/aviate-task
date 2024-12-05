# Generated by Django 4.2.17 on 2024-12-04 22:39

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("candidates", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="candidate",
            name="age",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="candidate",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                max_length=1,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="candidate",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True, max_length=128, null=True, region=None
            ),
        ),
    ]
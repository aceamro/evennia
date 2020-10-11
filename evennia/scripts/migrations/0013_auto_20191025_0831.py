# Generated by Django 2.2.6 on 2019-10-25 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("scripts", "0012_auto_20190128_1820")]

    operations = [
        migrations.AlterField(
            model_name="scriptdb",
            name="db_typeclass_path",
            field=models.CharField(
                db_index=True,
                help_text="this defines what 'type' of entity this is. This variable holds a Python path to a module with a valid Evennia Typeclass.",
                max_length=255,
                null=True,
                verbose_name="typeclass",
            ),
        )
    ]
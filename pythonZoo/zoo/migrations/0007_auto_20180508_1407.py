# Generated by Django 2.0.4 on 2018-05-08 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0006_auto_20180501_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibit',
            name='zoo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parentZoo', to='zoo.Zoo'),
        ),
    ]
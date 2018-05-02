# Generated by Django 2.0.4 on 2018-05-01 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0005_animals'),
    ]

    operations = [
        migrations.AddField(
            model_name='animals',
            name='dietDesc',
            field=models.TextField(help_text='Enter a Description', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='animals',
            name='habitatDesc',
            field=models.TextField(help_text='Enter a Description', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='animals',
            name='imageFilePath',
            field=models.CharField(help_text='Enter Image Path', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='animals',
            name='soundFilePath',
            field=models.CharField(help_text='Enter Sound Path', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='animals',
            name='name',
            field=models.CharField(help_text='Enter Animal Name', max_length=200, null=True),
        ),
    ]
